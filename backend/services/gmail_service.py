import asyncio
import logging
import os
import os.path
import ssl

import chromadb
import google_auth_httplib2
import httplib2
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
from services.progress_display import (
    NewsletterContext,
    PipelineProgressTracker,
    Stage,
    set_newsletter_ctx,
)

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


def _get_gmail_credentials() -> Credentials:
    """Return valid Gmail OAuth2 credentials, refreshing or re-authorising as needed.

    The credentials are read from ``token.json`` (created on first auth).
    This function is lightweight after the initial authorisation flow.
    """
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=8080)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def gmail_authenticate():
    """Authenticate with the Gmail API and return the service."""
    try:
        creds = _get_gmail_credentials()
        return build("gmail", "v1", credentials=creds)
    except HttpError as e:
        logger.error(f"Gmail API HttpError during authentication: {e}")
        raise
    except Exception as e:
        logger.error(f"Unexpected error during Gmail authentication: {e}")
        raise


async def sync_state_to_model(latest_email_id: str) -> SyncState:
    """Convert the sync state to a model (with retry on transient errors).

    Args:
        latest_email_id: Gmail message ID of the latest synced email.

    Returns:
        SyncState: The sync state model
    """
    service = gmail_authenticate()
    latest_email = await _fetch_gmail_message_with_retry(service, latest_email_id)
    return SyncState(
        gmail_message_id=latest_email_id,
        subject=get_item_from_gmail_response(latest_email, "subject") or "",
        sender_name=parse_sender(
            get_item_from_gmail_response(latest_email, "sender") or ""
        )["name"],
        sender_email=parse_sender(
            get_item_from_gmail_response(latest_email, "sender") or ""
        )["email"],
        last_synced_internal_date=int(
            get_item_from_gmail_response(latest_email, "internal_date") or 0
        ),
    )


async def newsletter_to_model(newsletter_data: dict) -> Newsletter:
    """Convert the newsletter data to a model
    Args:
        newsletter_data (dict): The newsletter data
    Returns:
        Newsletter: The newsletter model
    """
    sender_info = parse_sender(
        get_item_from_gmail_response(newsletter_data, "sender") or ""
    )
    raw_md = html_to_markdown(newsletter_data)  # clean markdown text
    log_info = [
        sender_info["name"],
        sender_info["email"],
        convert_internal_date_to_datetime(
            int(get_item_from_gmail_response(newsletter_data, "internal_date") or 0)
        ),
    ]
    cleaned_md = await llm_clean_up(raw_md, log_info)

    # Only embed if we got cleaned markdown
    cleaned_md_embedding = None
    if cleaned_md:
        cleaned_md_embedding = await embed_newsletter(cleaned_md)

    return Newsletter(
        _id=str(get_item_from_gmail_response(newsletter_data, "id")),
        thread_id=get_item_from_gmail_response(newsletter_data, "thread_id") or "",
        history_id=get_item_from_gmail_response(newsletter_data, "history_id"),
        internal_date=int(
            get_item_from_gmail_response(newsletter_data, "internal_date") or 0
        ),
        received_datetime=convert_internal_date_to_datetime(
            int(get_item_from_gmail_response(newsletter_data, "internal_date") or 0)
        ).strftime("%Y-%m-%d"),
        sender_name=sender_info["name"],
        sender_email=sender_info["email"],
        subject=get_item_from_gmail_response(newsletter_data, "subject") or "",
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

        # fetch newsletters from query (with retry on SSL/transient errors)
        logger.info(f"(*) Fetching newsletters using query: {query}")
        next_page_token = None
        while True:
            try:
                gmail_fetch_result = await _gmail_execute_with_retry(
                    lambda pt=next_page_token: service.users()
                    .messages()
                    .list(userId="me", q=query, pageToken=pt)
                    .execute(),
                    operation_name="messages.list",
                )
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


def _is_transient_error(exception: BaseException) -> bool:
    """Check if an exception is a transient/retriable error (e.g. SSL, network)."""
    err_str = str(exception).lower()
    return (
        "ssl" in err_str
        or "record layer failure" in err_str
        or "connection reset" in err_str
        or "connection refused" in err_str
        or "connection aborted" in err_str
        or "timeout" in err_str
        or "timed out" in err_str
        or "temporary failure" in err_str
        or "service unavailable" in err_str
        or "handshake" in err_str
        or "decryption" in err_str
        or "certificate" in err_str
        or "eof occurred" in err_str
        or "wrong_version_number" in err_str
        or "transient" in err_str
        or isinstance(exception, (ssl.SSLError, ConnectionError, TimeoutError))
    )


async def _gmail_execute_with_retry(
    thunk,
    *,
    max_retries: int = 5,
    base_delay: float = 2.0,
    operation_name: str = "Gmail API",
    creds: Credentials | None = None,
):
    """Run a sync Gmail API call with retry on transient errors.

    If *creds* is supplied the caller should pass a *thunk* that returns an
    ``HttpRequest`` (i.e. **without** calling ``.execute()``).  This function
    will then execute it with a fresh ``AuthorizedHttp`` transport per attempt,
    making the call thread-safe for concurrent ``asyncio.to_thread`` usage.

    If *creds* is ``None`` the thunk is called as before (it should call
    ``.execute()`` itself).

    Args:
        thunk: No-arg callable.  When *creds* is provided it should return an
            ``HttpRequest``; otherwise it should perform the full API call.
        max_retries: Maximum retry attempts.
        base_delay: Base delay in seconds for exponential backoff.
        operation_name: Label for logging.
        creds: Optional OAuth2 credentials for thread-safe HTTP.

    Returns:
        The API response.

    Raises:
        Exception: If all retries are exhausted.
    """
    last_exception = None
    for attempt in range(max_retries + 1):
        try:
            if creds:

                def _safe_execute():
                    request = thunk()
                    http = google_auth_httplib2.AuthorizedHttp(
                        creds, http=httplib2.Http()
                    )
                    return request.execute(http=http)

                return await asyncio.to_thread(_safe_execute)
            else:
                return await asyncio.to_thread(thunk)
        except Exception as e:
            last_exception = e
            if _is_transient_error(e) and attempt < max_retries:
                delay = base_delay * (2**attempt)
                logger.warning(
                    f"Transient error in {operation_name} "
                    f"(attempt {attempt + 1}/{max_retries + 1}): {e}. "
                    f"Retrying in {delay:.1f}s..."
                )
                await asyncio.sleep(delay)
            else:
                raise
    raise last_exception  # type: ignore


async def _fetch_gmail_message_with_retry(
    service,
    message_id: str,
    creds: Credentials | None = None,
    max_retries: int = 5,
    base_delay: float = 2.0,
) -> dict:
    """Fetch a Gmail message with retry on transient errors.

    When *creds* is supplied, each attempt builds a fresh
    ``google_auth_httplib2.AuthorizedHttp`` transport so that concurrent
    ``asyncio.to_thread`` calls do not share the same ``httplib2.Http``
    connection (the default connection inside *service* is **not**
    thread-safe and causes ``'NoneType' object has no attribute 'read'``
    / ``'close'`` errors under concurrency).

    Args:
        service: Gmail API service (used to build the request object).
        message_id: The message ID to fetch.
        creds: Optional OAuth2 credentials for thread-safe HTTP.
        max_retries: Maximum retry attempts.
        base_delay: Base delay in seconds for exponential backoff.

    Returns:
        The message data dict.

    Raises:
        Exception: If all retries are exhausted.
    """
    last_exception = None

    for attempt in range(max_retries + 1):
        try:

            def _fetch() -> dict:
                request = (
                    service.users()
                    .messages()
                    .get(userId="me", id=message_id)
                )
                if creds:
                    # Thread-safe: fresh HTTP transport per call
                    http = google_auth_httplib2.AuthorizedHttp(
                        creds, http=httplib2.Http()
                    )
                    return request.execute(http=http)
                return request.execute()

            return await asyncio.to_thread(_fetch)
        except Exception as e:
            last_exception = e
            if _is_transient_error(e) and attempt < max_retries:
                delay = base_delay * (2**attempt)
                logger.warning(
                    f"Transient error fetching message {message_id} "
                    f"(attempt {attempt + 1}/{max_retries + 1}): {e}. "
                    f"Retrying in {delay:.1f}s..."
                )
                await asyncio.sleep(delay)
            else:
                raise

    raise last_exception  # type: ignore


async def _process_single_newsletter(
    service,
    chroma_client,
    newsletter_id: dict,
    index: int,
    total: int,
    semaphore: asyncio.Semaphore,
    tracker: PipelineProgressTracker | None = None,
    creds: Credentials | None = None,
) -> tuple[bool, str | None]:
    """Process a single newsletter with concurrency control.

    Args:
        service: Gmail API service
        chroma_client: ChromaDB client
        newsletter_id: Dict with newsletter id
        index: Current index for logging
        total: Total count for logging
        semaphore: Semaphore for concurrency control
        tracker: Optional Rich progress tracker for live display
        creds: Optional OAuth2 credentials for thread-safe Gmail calls

    Returns:
        Tuple of (success: bool, error_message: str | None)
    """
    msg_id = newsletter_id["id"]

    # Set up newsletter context for genai retry callbacks
    nl_ctx = NewsletterContext(msg_id, f"#{index + 1}")
    ctx_token = set_newsletter_ctx(nl_ctx)

    async with semaphore:
        try:
            # --- Stage 1: Fetch ---
            if tracker:
                tracker.update_stage(msg_id, Stage.FETCHING)
            newsletter_data = await _fetch_gmail_message_with_retry(
                service, msg_id, creds=creds
            )

            # Now we know the sender – update the display label
            sender_info = parse_sender(
                get_item_from_gmail_response(newsletter_data, "sender") or ""
            )
            sender_label = sender_info["name"] or sender_info["email"] or msg_id
            nl_ctx.label = sender_label
            if tracker:
                tracker.update_sender(msg_id, sender_label)
            else:
                logger.info(
                    f"(*) Processing newsletter {index + 1} of {total} =========================="
                )

            # --- Stage 2: Dedup check ---
            if tracker:
                tracker.update_stage(msg_id, Stage.DEDUP_CHECK)
            if await get_newsletter(newsletter_data["id"]):
                if not tracker:
                    logger.info(f"Newsletter already exists: {newsletter_data['id']}")
                if tracker:
                    tracker.mark_skipped(msg_id)
                return (True, None)

            # --- Stage 3: HTML -> Markdown ---
            if tracker:
                tracker.update_stage(msg_id, Stage.HTML_TO_MD)
            raw_md = html_to_markdown(newsletter_data)

            log_info = [
                sender_info["name"],
                sender_info["email"],
                convert_internal_date_to_datetime(
                    int(
                        get_item_from_gmail_response(
                            newsletter_data, "internal_date"
                        )
                        or 0
                    )
                ),
            ]

            # --- Stage 4: LLM Cleanup ---
            if tracker:
                tracker.update_stage(msg_id, Stage.LLM_CLEANUP)
            cleaned_md = await llm_clean_up(raw_md, log_info)

            # --- Stage 5: Embedding ---
            cleaned_md_embedding = None
            if cleaned_md:
                if tracker:
                    tracker.update_stage(msg_id, Stage.EMBEDDING)
                cleaned_md_embedding = await embed_newsletter(cleaned_md)

            # Build the Newsletter model
            newsletter = Newsletter(
                _id=str(get_item_from_gmail_response(newsletter_data, "id")),
                thread_id=get_item_from_gmail_response(
                    newsletter_data, "thread_id"
                )
                or "",
                history_id=get_item_from_gmail_response(
                    newsletter_data, "history_id"
                ),
                internal_date=int(
                    get_item_from_gmail_response(
                        newsletter_data, "internal_date"
                    )
                    or 0
                ),
                received_datetime=convert_internal_date_to_datetime(
                    int(
                        get_item_from_gmail_response(
                            newsletter_data, "internal_date"
                        )
                        or 0
                    )
                ).strftime("%Y-%m-%d"),
                sender_name=sender_info["name"],
                sender_email=sender_info["email"],
                subject=get_item_from_gmail_response(
                    newsletter_data, "subject"
                )
                or "",
                raw_html=get_item_from_gmail_response(newsletter_data, "html"),
                raw_md=raw_md,
                cleaned_md=cleaned_md,
                cleaned_md_embedding=cleaned_md_embedding,
            )

            # --- Stage 6: Save to DB ---
            if tracker:
                tracker.update_stage(msg_id, Stage.SAVE_DB)
            await upsert_newsletter(newsletter)
            await add_newsletter_to_chroma_collection(chroma_client, newsletter)

            # --- Stage 7: Complete ---
            if tracker:
                tracker.mark_complete(msg_id)
            return (True, None)

        except HttpError as e:
            error_msg = (
                f"Gmail API HttpError processing newsletter {msg_id}: {e}"
            )
            if tracker:
                tracker.mark_failed(msg_id, str(e))
            else:
                logger.error(error_msg)
            return (False, error_msg)
        except Exception as e:
            error_msg = f"Error processing newsletter {msg_id}: {e}"
            if tracker:
                tracker.mark_failed(msg_id, str(e))
            else:
                logger.error(error_msg)
            return (False, error_msg)
        finally:
            set_newsletter_ctx(None)
            ctx_token  # keep reference to avoid unused-variable linting


async def process_fetched_newsletters(
    fetched_newsletters_ids: list,
    max_concurrent: int | None = None,
    use_rich: bool = False,
) -> dict:
    """Process the newsletter data with concurrent processing.

    Args:
        fetched_newsletters_ids: The fetched newsletters ids
        max_concurrent: Max concurrent newsletter processing (defaults to gemini_max_concurrent)
        use_rich: If True, show a Rich live progress display in the terminal

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

        # Authenticate – obtain credentials *and* service separately so that
        # concurrent tasks can create per-thread HTTP transports from creds.
        creds = _get_gmail_credentials()
        service = build("gmail", "v1", credentials=creds)

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

        # --- Optionally create the Rich progress tracker ---
        tracker: PipelineProgressTracker | None = None
        if use_rich:
            tracker = PipelineProgressTracker(
                total_newsletters=total, max_concurrent=concurrent_limit
            )

        async def _run_processing(
            trk: PipelineProgressTracker | None,
        ) -> list:
            # Pre-register all newsletters in the display
            if trk:
                for i, nl_id in enumerate(fetched_newsletters_ids):
                    trk.add_newsletter(
                        nl_id["id"],
                        label=f"Newsletter {i + 1}",
                        index=i + 1,
                    )

            # Create tasks for all newsletters
            tasks = [
                _process_single_newsletter(
                    service,
                    chroma_client,
                    newsletter_id,
                    i,
                    total,
                    semaphore,
                    tracker=trk,
                    creds=creds,
                )
                for i, newsletter_id in enumerate(fetched_newsletters_ids)
            ]

            return await asyncio.gather(*tasks, return_exceptions=True)

        # Execute with or without the Rich context manager
        if tracker:
            async with tracker:
                results = await _run_processing(tracker)
        else:
            results = await _run_processing(None)

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

        # Update sync state only if no failed (with retry on transient errors)
        if failed == 0:
            try:
                list_result = await _gmail_execute_with_retry(
                    lambda: service.users().messages().list(userId="me"),
                    operation_name="messages.list(sync state)",
                    creds=creds,
                )
                latest_email_id = list_result["messages"][0]["id"]
                latest_sync_state = await sync_state_to_model(latest_email_id)
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
    tracker: PipelineProgressTracker | None = None,
) -> tuple[bool, str | None]:
    """Retry cleanup for a single newsletter with concurrency control.

    Args:
        newsletter: The newsletter to retry
        semaphore: Semaphore for concurrency control
        tracker: Optional Rich progress tracker for live display

    Returns:
        Tuple of (success: bool, error_message: str | None)
    """
    nl_id = str(newsletter.id)
    nl_ctx = NewsletterContext(nl_id, newsletter.sender_name or nl_id)
    ctx_token = set_newsletter_ctx(nl_ctx)

    async with semaphore:
        try:
            # Check if raw_md exists
            if not newsletter.raw_md:
                if tracker:
                    tracker.mark_failed(nl_id, "No raw_md to clean")
                return (False, f"Newsletter {newsletter.id} has no raw_md to clean")

            log_info = [
                newsletter.sender_name,
                newsletter.sender_email,
                newsletter.received_datetime,
            ]

            # --- Stage: LLM Cleanup ---
            if tracker:
                tracker.update_stage(nl_id, Stage.LLM_CLEANUP)
            retried_cleaned_md = await llm_clean_up(newsletter.raw_md, log_info)

            if not retried_cleaned_md:
                if tracker:
                    tracker.mark_failed(nl_id, "Empty LLM response")
                return (
                    False,
                    f"Failed to clean newsletter {newsletter.id}: empty response",
                )

            newsletter.cleaned_md = retried_cleaned_md

            # --- Stage: Embedding ---
            if tracker:
                tracker.update_stage(nl_id, Stage.EMBEDDING)
            newsletter.cleaned_md_embedding = await embed_newsletter(retried_cleaned_md)

            # --- Stage: Save ---
            if tracker:
                tracker.update_stage(nl_id, Stage.SAVE_DB)
            await upsert_newsletter(newsletter)

            if tracker:
                tracker.mark_complete(nl_id)
            else:
                logger.info(f"Successfully retried cleanup for newsletter {newsletter.id}")
            return (True, None)

        except Exception as e:
            error_msg = f"Error retrying cleaned_md for newsletter {newsletter.id}: {e}"
            if tracker:
                tracker.mark_failed(nl_id, str(e))
            else:
                logger.error(error_msg)
            return (False, error_msg)
        finally:
            set_newsletter_ctx(None)
            ctx_token  # keep reference to avoid unused-variable linting


async def retry_null_cleaned_md(
    max_concurrent: int | None = None,
    use_rich: bool = False,
) -> dict:
    """Retry cleaning newsletters that have null cleaned_md with concurrent processing.

    Args:
        max_concurrent: Max concurrent retries (defaults to gemini_max_concurrent)
        use_rich: If True, show a Rich live progress display in the terminal

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

        # --- Optionally create the Rich progress tracker ---
        tracker: PipelineProgressTracker | None = None
        if use_rich:
            tracker = PipelineProgressTracker(
                total_newsletters=total, max_concurrent=concurrent_limit
            )

        async def _run_retries(
            trk: PipelineProgressTracker | None,
        ) -> list:
            # Pre-register all newsletters (start at LLM_CLEANUP stage)
            if trk:
                for i, nl in enumerate(null_cleaned_md_newsletters):
                    trk.add_newsletter(
                        str(nl.id),
                        label=nl.sender_name or str(nl.id),
                        index=i + 1,
                    )

            tasks = [
                _retry_single_newsletter_cleanup(newsletter, semaphore, tracker=trk)
                for newsletter in null_cleaned_md_newsletters
            ]
            return await asyncio.gather(*tasks, return_exceptions=True)

        if tracker:
            async with tracker:
                results = await _run_retries(tracker)
        else:
            results = await _run_retries(None)

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
        # process fetched newsletters (Rich progress display enabled)
        await process_fetched_newsletters(
            fetched_newsletters_ids["results"], use_rich=True
        )
        # retry null cleaned md (Rich progress display enabled)
        await retry_null_cleaned_md(use_rich=True)
        # stop db
        await disconnect_from_mongo()

    asyncio.run(test_run())
