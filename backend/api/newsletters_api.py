from config import settings
from database.database import get_collection_names
from fastapi import APIRouter, BackgroundTasks, HTTPException
from models.newsletter import Newsletter
from services import gmail_service

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "FastAPI + MongoDB App"}


@router.get("/db-test")
async def test_db_connection():
    try:
        # Test the connection by listing collections
        print(settings.database_name)
        collections = await get_collection_names(settings.database_name)
        return {"status": "success", "collections": collections}
    except Exception as e:
        return {"status": "error", "message": str(e)}


@router.get("/gmail-api-test")
async def gmail_api_test():
    service = gmail_service.gmail_authenticate()
    results = service.users().messages().list(userId="me").execute()
    print(results)
    return {"message": "Gmail API test", "results": results}


@router.get("/target-newsletters-ids-TEST")
async def target_newsletters_ids_test():
    try:
        response = await gmail_service.fetch_new_newsletters_ids()
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/list")  # List or search newsletters (perhaps with query params)
async def list_newsletters():
    # TODO: Implement database fetching
    # Fetch from database (e.g., using Motor)
    return {"newsletters": []}


@router.post(
    "/ingest"
)  # Endpoint to ingest a new email (via webhook or manual trigger)
async def ingest_newsletter(background_tasks: BackgroundTasks):
    """Triggered by Gmail push or manual call to process new emails."""
    # In a push scenario, Gmail would call this with minimal data, then we fetch email:
    background_tasks.add_task(gmail_service.fetch_and_process_latest)
    return {
        "status": "accepted"
    }  # respond quickly, actual processing happens in background


@router.post("/")  # Endpoint to add a newsletter manually (for example)
async def add_newsletter(newsletter: Newsletter, background_tasks: BackgroundTasks):
    # TODO: Implement database saving and summarization
    # Save the raw newsletter to DB and trigger background summarization
    newsletter_doc = newsletter.model_dump(exclude={"summary"})

    # TODO: Save to database
    # background_tasks.add_task(summarize_newsletter, newsletter_doc)

    return {"message": "Newsletter received, processing not yet implemented."}
