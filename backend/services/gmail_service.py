import asyncio
import logging
import os
import os.path

import chromadb
from config import settings
from database.database import (
    add_newsletter_to_chroma_collection,
    connect_to_mongo,
    disconnect_from_mongo,
    get_newsletter,
    get_null_cleaned_md_newsletters,
    get_sync_state,
    upsert_newsletter,
    upsert_sync_state,
)
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from helpers.helpers import (
    convert_internal_date_to_datetime,
    get_item_from_gmail_response,
    parse_sender,
)
from models.newsletter import Newsletter
from models.sync_state import SyncState
from services.genai_service import embed_newsletter, llm_clean_up
from services.pre_processing_service import html_to_markdown

# ------------------------------
# Logger
# ------------------------------
# capture module name and set level
logger = logging.getLogger(__name__)
logger.setLevel(settings.logger_level)

# Create console handler (stream logger to console) and set level to debug
console_handler = logging.StreamHandler()
console_handler.setLevel(settings.logger_level)  # Capture all levels

# Create formatter and add it to the handler
formatter = logging.Formatter(
    "\n[%(asctime)s] %(levelname)s in [%(module)s]: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
console_handler.setFormatter(formatter)

# Add the handler to the logger if not already added
if not logger.hasHandlers():
    logger.addHandler(console_handler)

# ------------------------------
# Gmail Service
# ------------------------------
# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def gmail_authenticate():
    """Authenticate with the Gmail API and return the service."""
    try:
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists("token.json"):
            creds = Credentials.from_authorized_user_file("token.json", SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "credentials.json", SCOPES
                )
                creds = flow.run_local_server(port=8080)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        return build("gmail", "v1", credentials=creds)
    except HttpError as e:
        logger.error(f"Gmail API HttpError during authentication: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during Gmail authentication: {e}")
        raise


def sync_state_to_model(latest_email_id: str) -> SyncState:
    """Convert the sync state to a model
    Args:
        newsletter_data (dict): The newsletter data
    Returns:
        SyncState: The sync state model
    """
    service = gmail_authenticate()
    latest_email = (
        service.users().messages().get(userId="me", id=latest_email_id).execute()
    )
    return SyncState(
        gmail_message_id=latest_email_id,
        subject=get_item_from_gmail_response(latest_email, "subject"),
        sender_name=parse_sender(get_item_from_gmail_response(latest_email, "sender"))[
            "name"
        ],
        sender_email=parse_sender(get_item_from_gmail_response(latest_email, "sender"))[
            "email"
        ],
        last_synced_internal_date=get_item_from_gmail_response(
            latest_email, "internal_date"
        ),
    )


async def newsletter_to_model(newsletter_data: dict) -> Newsletter:
    """Convert the newsletter data to a model
    Args:
        newsletter_data (dict): The newsletter data
    Returns:
        Newsletter: The newsletter model
    """
    sender_info = parse_sender(get_item_from_gmail_response(newsletter_data, "sender"))
    raw_md = html_to_markdown(newsletter_data)  # clean markdown text
    log_info = [
        sender_info["name"],
        sender_info["email"],
        convert_internal_date_to_datetime(
            int(get_item_from_gmail_response(newsletter_data, "internal_date"))
        ),
    ]
    cleaned_md = await llm_clean_up(raw_md, log_info)

    # Only embed if we got cleaned markdown
    cleaned_md_embedding = None
    if cleaned_md:
        cleaned_md_embedding = await embed_newsletter(cleaned_md)

    return Newsletter(
        id=get_item_from_gmail_response(newsletter_data, "id"),
        thread_id=get_item_from_gmail_response(newsletter_data, "thread_id"),
        history_id=get_item_from_gmail_response(newsletter_data, "history_id"),
        internal_date=get_item_from_gmail_response(newsletter_data, "internal_date"),
        received_datetime=convert_internal_date_to_datetime(
            int(get_item_from_gmail_response(newsletter_data, "internal_date"))
        ).strftime("%Y-%m-%d"),
        sender_name=sender_info["name"],
        sender_email=sender_info["email"],
        subject=get_item_from_gmail_response(newsletter_data, "subject"),
        raw_html=get_item_from_gmail_response(newsletter_data, "html"),
        raw_md=raw_md,
        cleaned_md=cleaned_md,
        cleaned_md_embedding=cleaned_md_embedding,
    )


async def fetch_new_newsletters_ids():
    """Fetch the latest newsletter from Gmail and process it (save + summarize).
    Returns:
        dict: {
            "message": "Fetch newsletters from Gmail API",
            "results": {
                "sender_email": {}
            }
        }
    """
    try:
        service = gmail_authenticate()
        # sync state
        sync_state = await get_sync_state()
        fetched_newsletter_ids = []
        query = ""
        if not sync_state:  # first time run
            # construct query from target newsletters
            query = " OR ".join(
                [
                    f'from:"{sender_info["name"]}"'
                    for sender_info in settings.target_newsletters
                ]
            )
        else:  # subsequent runs that will start from the last sync state
            # construct query from target newsletters
            query = " OR ".join(
                [
                    f'from:"{sender_info["name"]}"'
                    for sender_info in settings.target_newsletters
                ]
            )
            # add 5 seconds to the last synced internal date to avoid duplicates
            query = f"after:{int(sync_state.last_synced_internal_date / 1000) + 5} AND {query}"

        # fetch newsletters from query
        logger.info(f"(*) Fetching newsletters using query: {query}")
        next_page_token = None
        while True:
            try:
                request = (
                    service.users()
                    .messages()
                    .list(
                        userId="me",
                        q=query,
                        pageToken=next_page_token,
                    )
                )
                gmail_fetch_result = request.execute()
                if "messages" in gmail_fetch_result:
                    fetched_newsletter_ids.extend(gmail_fetch_result["messages"])
                next_page_token = gmail_fetch_result.get("nextPageToken")
                if not next_page_token:
                    break
            except HttpError as e:
                logger.error(f"Gmail API HttpError during fetch: {e}")
                break
            except Exception as e:
                logger.error(f"Unexpected error during fetch: {e}")
                break

        # fetch result
        fetch_result = {
            "message": "Fetch newsletters from Gmail API",
            "results": fetched_newsletter_ids,
            "count": len(fetched_newsletter_ids),
        }
        logger.info(f"(*) Fetched {fetch_result['count']} newsletters")
        return fetch_result
    except Exception as e:
        logger.error(f"Error in fetch_new_newsletters_ids: {e}")
        return {"message": "Error fetching newsletters", "results": [], "count": 0}


async def _process_single_newsletter(
    service,
    chroma_client,
    newsletter_id: dict,
    index: int,
    total: int,
    semaphore: asyncio.Semaphore,
) -> tuple[bool, str | None]:
    """Process a single newsletter with concurrency control.

    Args:
        service: Gmail API service
        chroma_client: ChromaDB client
        newsletter_id: Dict with newsletter id
        index: Current index for logging
        total: Total count for logging
        semaphore: Semaphore for concurrency control

    Returns:
        Tuple of (success: bool, error_message: str | None)
    """
    async with semaphore:
        try:
            # Fetch newsletter data (sync call, run in thread)
            newsletter_data = await asyncio.to_thread(
                lambda: service.users()
                .messages()
                .get(userId="me", id=newsletter_id["id"])
                .execute()
            )

            logger.info(
                f"(*) Processing newsletter {index + 1} of {total} =========================="
            )

            # Check if newsletter already exists
            if await get_newsletter(newsletter_data["id"]):
                logger.info(f"Newsletter already exists: {newsletter_data['id']}")
                return (True, None)

            # Convert to pydantic model (includes LLM cleanup and embedding)
            newsletter: Newsletter = await newsletter_to_model(newsletter_data)

            # Save to db
            await upsert_newsletter(newsletter)

            # Save to chromadb
            await add_newsletter_to_chroma_collection(chroma_client, newsletter)

            return (True, None)

        except HttpError as e:
            error_msg = (
                f"Gmail API HttpError processing newsletter {newsletter_id['id']}: {e}"
            )
            logger.error(error_msg)
            return (False, error_msg)
        except Exception as e:
            error_msg = f"Error processing newsletter {newsletter_id['id']}: {e}"
            logger.error(error_msg)
            return (False, error_msg)


async def process_fetched_newsletters(
    fetched_newsletters_ids: list,
    max_concurrent: int | None = None,
) -> dict:
    """Process the newsletter data with concurrent processing.

    Args:
        fetched_newsletters_ids: The fetched newsletters ids
        max_concurrent: Max concurrent newsletter processing (defaults to gemini_max_concurrent)

    Returns:
        Dict with processing results
    """
    if not fetched_newsletters_ids:
        logger.info("No newsletters to process")
        return {"processed": 0, "failed": 0, "errors": []}

    try:
        # Use configured concurrency or override
        concurrent_limit = max_concurrent or settings.gemini_max_concurrent
        semaphore = asyncio.Semaphore(concurrent_limit)

        # Authenticate
        service = gmail_authenticate()

        # ChromaDB client
        chroma_client = chromadb.CloudClient(
            api_key=settings.chromadb_api_key,
            tenant=settings.chromadb_tenant,
            database=settings.chromadb_database,
        )

        total = len(fetched_newsletters_ids)
        logger.info(
            f"Processing {total} newsletters with max {concurrent_limit} concurrent"
        )

        # Create tasks for all newsletters
        tasks = [
            _process_single_newsletter(
                service, chroma_client, newsletter_id, i, total, semaphore
            )
            for i, newsletter_id in enumerate(fetched_newsletters_ids)
        ]

        # Process concurrently
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Collect results
        processed = 0
        failed = 0
        errors = []

        for i, result in enumerate(results):
            if isinstance(result, Exception):
                failed += 1
                errors.append(
                    f"Newsletter {fetched_newsletters_ids[i]['id']}: {result}"
                )
            elif isinstance(result, tuple):
                success, error = result
                if success:
                    processed += 1
                else:
                    failed += 1
                    if error:
                        errors.append(error)

        logger.info(f"Processing complete: {processed} succeeded, {failed} failed")

        # Update sync state if any succeeded
        if processed > 0:
            try:
                latest_email_id = (
                    service.users()
                    .messages()
                    .list(userId="me")
                    .execute()["messages"][0]["id"]
                )
                latest_sync_state = sync_state_to_model(latest_email_id)
                await upsert_sync_state(latest_sync_state)
            except Exception as e:
                logger.error(f"Failed to update sync state: {e}")

        return {"processed": processed, "failed": failed, "errors": errors}

    except Exception as e:
        logger.error(f"Error in process_fetched_newsletters: {e}")
        return {
            "processed": 0,
            "failed": len(fetched_newsletters_ids),
            "errors": [str(e)],
        }


async def _retry_single_newsletter_cleanup(
    newsletter: Newsletter,
    semaphore: asyncio.Semaphore,
) -> tuple[bool, str | None]:
    """Retry cleanup for a single newsletter with concurrency control.

    Args:
        newsletter: The newsletter to retry
        semaphore: Semaphore for concurrency control

    Returns:
        Tuple of (success: bool, error_message: str | None)
    """
    async with semaphore:
        try:
            # Check if raw_md exists
            if not newsletter.raw_md:
                return (False, f"Newsletter {newsletter.id} has no raw_md to clean")

            log_info = [
                newsletter.sender_name,
                newsletter.sender_email,
                newsletter.received_datetime,
            ]

            retried_cleaned_md = await llm_clean_up(newsletter.raw_md, log_info)

            if not retried_cleaned_md:
                return (
                    False,
                    f"Failed to clean newsletter {newsletter.id}: empty response",
                )

            newsletter.cleaned_md = retried_cleaned_md

            # Also generate embedding for the cleaned markdown
            newsletter.cleaned_md_embedding = await embed_newsletter(retried_cleaned_md)

            await upsert_newsletter(newsletter)

            logger.info(f"Successfully retried cleanup for newsletter {newsletter.id}")
            return (True, None)

        except Exception as e:
            error_msg = f"Error retrying cleaned_md for newsletter {newsletter.id}: {e}"
            logger.error(error_msg)
            return (False, error_msg)


async def retry_null_cleaned_md(max_concurrent: int | None = None) -> dict:
    """Retry cleaning newsletters that have null cleaned_md with concurrent processing.

    Args:
        max_concurrent: Max concurrent retries (defaults to gemini_max_concurrent)

    Returns:
        Dict with retry results
    """
    try:
        null_cleaned_md_newsletters = await get_null_cleaned_md_newsletters()

        if not null_cleaned_md_newsletters:
            logger.info("No newsletters with null cleaned_md to retry")
            return {"retried": 0, "failed": 0, "errors": []}

        concurrent_limit = max_concurrent or settings.gemini_max_concurrent
        semaphore = asyncio.Semaphore(concurrent_limit)

        total = len(null_cleaned_md_newsletters)
        logger.info(
            f"Retrying {total} newsletters with max {concurrent_limit} concurrent"
        )

        # Create tasks for all newsletters
        tasks = [
            _retry_single_newsletter_cleanup(newsletter, semaphore)
            for newsletter in null_cleaned_md_newsletters
        ]

        # Process concurrently
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Collect results
        retried = 0
        failed = 0
        errors = []

        for i, result in enumerate(results):
            if isinstance(result, Exception):
                failed += 1
                errors.append(
                    f"Newsletter {null_cleaned_md_newsletters[i].id}: {result}"
                )
            elif isinstance(result, tuple):
                success, error = result
                if success:
                    retried += 1
                else:
                    failed += 1
                    if error:
                        errors.append(error)

        logger.info(f"Retry complete: {retried} succeeded, {failed} failed")
        return {"retried": retried, "failed": failed, "errors": errors}

    except Exception as e:
        logger.error(f"Error in retry_null_cleaned_md: {e}")
        return {"retried": 0, "failed": 0, "errors": [str(e)]}


if __name__ == "__main__":
    import asyncio

    async def test_run():
        # start db
        await connect_to_mongo()
        # test fetch_new_newsletters_ids
        fetched_newsletters_ids = await fetch_new_newsletters_ids()
        # process fetched newsletters
        await process_fetched_newsletters(fetched_newsletters_ids["results"])
        # retry null cleaned md
        await retry_null_cleaned_md()
        # stop db
        await disconnect_from_mongo()

    asyncio.run(test_run())
