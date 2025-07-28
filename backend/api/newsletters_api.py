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
