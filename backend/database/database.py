from typing import Optional

from config import settings
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient


class Database:
    client: Optional[AsyncIOMotorClient] = None


db = Database()


# Async connection (recommended for FastAPI)
async def get_database() -> AsyncIOMotorClient:
    return db.client


async def connect_to_mongo():
    """Create database connection"""
    db.client = AsyncIOMotorClient(
        settings.mongodb_url,
        maxPoolSize=10,
        minPoolSize=10,
    )
    print("Connected to MongoDB")


async def close_mongo_connection():
    """Close database connection"""
    if db.client:
        db.client.close()
        print("Disconnected from MongoDB")


async def get_database_names():
    """Get database names"""
    return await db.client.list_database_names()


async def get_collection_names(database_name: str):
    """Get collection names"""
    return await db.client[database_name].list_collection_names()


# For sync operations (if needed)
def get_sync_database():
    client = MongoClient(settings.mongodb_url)
    return client[settings.database_name]
