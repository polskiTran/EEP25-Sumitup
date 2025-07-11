import json
import logging
import os
import os.path
import time

import chromadb
from config import settings
from database.database import (
    add_newsletter_to_chroma_collection,
    close_mongo_connection,
    connect_to_mongo,
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
    construct_sender_info,
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
    cleaned_md_embedding = embed_newsletter(cleaned_md)
    return Newsletter(
        id=get_item_from_gmail_response(newsletter_data, "id"),
        thread_id=get_item_from_gmail_response(newsletter_data, "thread_id"),
        history_id=get_item_from_gmail_response(newsletter_data, "history_id"),
        internal_date=get_item_from_gmail_response(newsletter_data, "internal_date"),
        received_datetime=convert_internal_date_to_datetime(
            int(get_item_from_gmail_response(newsletter_data, "internal_date"))
        ),
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


async def process_fetched_newsletters(fetched_newsletters_ids: list):
    """Process the newsletter data
    Args:
        fetched_newsletters_ids (list): The fetched newsletters ids
    """
    try:
        error_flag = False
        # authenticate
        service = gmail_authenticate()
        # chromadb client
        client = chromadb.CloudClient(
            api_key=settings.chromadb_api_key,
            tenant=settings.chromadb_tenant,
            database=settings.chromadb_database,
        )

        # process fetched newsletters
        for i, newsletter_id in enumerate(fetched_newsletters_ids):
            try:
                # fetch newsletters from ids
                newsletter_data = (
                    service.users()
                    .messages()
                    .get(userId="me", id=newsletter_id["id"])
                    .execute()
                )
                # progress bar
                logger.info(
                    f"(*) Processing newsletter {i + 1} of {len(fetched_newsletters_ids)} =========================="
                )
                # check if newsletter already exists
                if await get_newsletter(newsletter_data["id"]):
                    logger.info(f"Newsletter already exists: {newsletter_data['id']}")
                    continue
                else:
                    # to pydantic model
                    newsletter: Newsletter = await newsletter_to_model(newsletter_data)
                # save to db
                await upsert_newsletter(newsletter)
                # save to chromadb
                await add_newsletter_to_chroma_collection(client, newsletter)
            except HttpError as e:
                logger.error(
                    f"Gmail API HttpError processing newsletter {newsletter_id['id']}: {e}"
                )
                continue
            except Exception as e:
                logger.error(f"Error processing newsletter {newsletter_id['id']}: {e}")
                error_flag = True
                break

        # capture latest fetched email id
        if not error_flag:
            latest_email_id = (
                service.users()
                .messages()
                .list(userId="me")
                .execute()["messages"][0]["id"]
            )
            latest_sync_state = sync_state_to_model(latest_email_id)
            await upsert_sync_state(latest_sync_state)
    except Exception as e:
        logger.error(f"Error in process_fetched_newsletters: {e}")


async def retry_null_cleaned_md():
    """Retry to clean the newsletter if the cleaned_md is null
    Args:
        newsletter (Newsletter): The newsletter model
    """
    try:
        null_cleaned_md_newsletters = await get_null_cleaned_md_newsletters()
        for newsletter in null_cleaned_md_newsletters:
            try:
                log_info = [
                    newsletter.sender_name,
                    newsletter.sender_email,
                    newsletter.received_datetime,
                ]
                retried_cleaned_md: str = await llm_clean_up(
                    newsletter.raw_md, log_info
                )
                if not retried_cleaned_md:
                    logger.error(
                        f"Failed to clean the newsletter: {newsletter.id}. Skipping..."
                    )
                    continue
                newsletter.cleaned_md = retried_cleaned_md
                await upsert_newsletter(newsletter)
            except Exception as e:
                logger.error(
                    f"Error retrying cleaned_md for newsletter {newsletter.id}: {e}"
                )
                continue
    except Exception as e:
        logger.error(f"Error in retry_null_cleaned_md: {e}")


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
        await close_mongo_connection()

    asyncio.run(test_run())
