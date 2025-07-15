import logging
from typing import List, Optional

import chromadb
from config import settings
from models.newsletter import Newsletter
from models.sync_state import SyncState
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection

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
# Async connection
# ------------------------------
class Database:
    client: Optional[AsyncIOMotorClient] = None


db = Database()


async def get_database() -> AsyncIOMotorClient:
    return db.client


async def connect_to_mongo():
    """Create database connection"""
    try:
        db.client = AsyncIOMotorClient(
            settings.mongodb_url,
            maxPoolSize=10,
            minPoolSize=10,
        )
        logger.info("(*) Connected to MongoDB --------------------------------\n")
    except Exception as e:
        logger.error(f"Error connecting to MongoDB: {e}\n")
        raise e


async def disconnect_from_mongo():
    """Close database connection"""
    try:
        if db.client:
            db.client.close()
            logger.info(
                "(*) Disconnected from MongoDB --------------------------------\n"
            )
    except Exception as e:
        logger.error(f"Error closing MongoDB connection: {e}\n")
        raise e


# ------------------------------
# Database Operations
# ------------------------------
async def get_database_names():
    """Get database names
    Returns:
        List[str]: The database names
    """
    return await db.client.list_database_names()


async def get_collection_names(database_name: str):
    """Get collection names
    Args:
        database_name (str): The name of the database to get collection names from
    Returns:
        List[str]: The collection names
    """
    return await db.client[database_name].list_collection_names()


def get_collection(collection_name: str) -> AsyncIOMotorCollection:
    """Get collection
    Args:
        collection_name (str): The name of the collection to get
    Returns:
        Collection: The collection
    """
    return db.client[settings.database_name][collection_name]


# ------------------------------
# Sync State Operations
# ------------------------------
async def get_sync_state():
    """Get the sync state
    Returns:
        SyncState: The sync state model
    """
    sync_state_collection = get_collection(settings.sync_state_collection_name)
    sync_state = await sync_state_collection.find_one()
    return SyncState(**sync_state) if sync_state else None


async def upsert_sync_state(new_sync_state: SyncState) -> SyncState:
    """Update the sync state
    Args:
        new_sync_state (SyncState): The sync state model
    Returns:
        SyncState: The updated sync state model
    """
    current_sync_state = await get_sync_state()
    if not current_sync_state:
        logger.info(
            f"Sync state not found, inserting: {new_sync_state.gmail_message_id}"
        )
    else:
        logger.info(f"Sync state found, updating: {new_sync_state.id}")
        # ensure monotonic internal date
        if (
            new_sync_state.last_synced_internal_date
            < current_sync_state.last_synced_internal_date
        ):
            raise ValueError(
                f"New sync state internal date is not greater than current sync state internal date: NEW: {new_sync_state.last_synced_internal_date} ({new_sync_state.sender_name} - {new_sync_state.gmail_message_id}) < CURRENT:  {current_sync_state.last_synced_internal_date} ({current_sync_state.sender_name} - {current_sync_state.gmail_message_id})"
            )
    try:
        await get_collection(settings.sync_state_collection_name).update_one(
            {"_id": settings.sync_state_id},
            {"$set": new_sync_state.model_dump(by_alias=True, exclude={"id"})},
            upsert=True,
        )
    except Exception as e:
        logger.error(f"Error updating sync state: {e}\n")
        raise e
    return await get_sync_state()


# ------------------------------
# Newsletter Operations
# ------------------------------
async def get_newsletter(gmail_message_id: str) -> Newsletter:
    """Get the newsletter
    Args:
        gmail_message_id (str): The gmail message id
    Returns:
        Newsletter: The newsletter model
    """
    try:
        if db.client is None:
            logger.error("Database client is not connected")
            raise Exception("Database client is not connected")
        newsletter_collection = get_collection(settings.newsletter_collection_name)
        newsletter = await newsletter_collection.find_one({"_id": gmail_message_id})
        return Newsletter(**newsletter) if newsletter else None
    except Exception as e:
        logger.error(f"Error getting newsletter: {e}")
        raise e


async def get_newsletters(filter: dict = {}) -> List[Newsletter]:
    """Get the newsletters
    Args:
        filter (dict): The filter to apply to the query
    Returns:
        List[Newsletter]: The newsletters models
    """
    try:
        if db.client is None:
            logger.error("Database client is not connected")
            raise Exception("Database client is not connected")
        newsletter_collection = get_collection(settings.newsletter_collection_name)
        newsletters = await newsletter_collection.find(filter).to_list(length=None)
        return [Newsletter(**newsletter) for newsletter in newsletters]
    except Exception as e:
        logger.error(f"Error getting newsletters: {e}")
        raise e


async def get_null_cleaned_md_newsletters():
    """Get the newsletters with null cleaned_md
    Returns:
        List[Newsletter]: The newsletters models
    """
    newsletter_collection = get_collection(settings.newsletter_collection_name)
    newsletters = await newsletter_collection.find({"cleaned_md": None}).to_list(
        length=None
    )
    logger.info(f"Found {len(newsletters)} newsletters with null cleaned_md")
    return [Newsletter(**newsletter) for newsletter in newsletters]


async def upsert_newsletter(newsletter: Newsletter) -> Newsletter:
    """Update the newsletter
    Args:
        newsletter (Newsletter): The newsletter model to be inserted or updated
    Returns:
        Newsletter: The updated newsletter model
    """
    current_newsletter = await get_newsletter(newsletter.id)
    if not current_newsletter:
        logger.info(f"Newsletter not found, inserting: {newsletter.id}")
    else:
        logger.info(f"Newsletter found, updating: {newsletter.id}")
    try:
        await get_collection(settings.newsletter_collection_name).update_one(
            {"_id": newsletter.id},
            {"$set": newsletter.model_dump(by_alias=True, exclude={"id"})},
            upsert=True,
        )
    except Exception as e:
        logger.error(f"Error updating newsletter: {e}")
        raise e
    return await get_newsletter(newsletter.id)


async def delete_newsletter(gmail_message_id: str):
    """Delete the newsletter
    Args:
        gmail_message_id (str): The gmail message id
    """
    current_newsletter = await get_newsletter(gmail_message_id)
    if not current_newsletter:
        raise ValueError("Newsletter not found")
    try:
        await get_collection(settings.newsletter_collection_name).delete_one(
            {"_id": gmail_message_id}
        )
        logger.info(f"Newsletter deleted: {gmail_message_id}")
    except Exception as e:
        logger.error(f"Error deleting newsletter: {e}")
        raise e


# ------------------------------
# ChromaDB Operations
# ------------------------------
async def add_newsletter_to_chroma_collection(
    client: chromadb.CloudClient, newsletter: Newsletter
):
    """Add the newsletter to the chroma collection
    Args:
        client (chromadb.CloudClient): The chroma client
        newsletter (Newsletter): The newsletter model
    """
    try:
        collection = client.get_collection(name=settings.chromadb_collection_name)
        collection.add(
            ids=[newsletter.id],
            documents=[newsletter.cleaned_md],
            metadatas=[
                {
                    "date": newsletter.received_datetime.strftime("%Y-%m-%d"),
                    "sender_name": newsletter.sender_name,
                    "sender_email": newsletter.sender_email,
                    "subject": newsletter.subject,
                }
            ],
        )
        logger.info(f"Newsletter added to chroma collection: {newsletter.id}")
    except Exception as e:
        logger.error(f"Error adding newsletter to chroma collection: {e}")
        raise e


if __name__ == "__main__":
    import asyncio

    async def main():
        await connect_to_mongo()
        # test delete_newsletter
        await get_null_cleaned_md_newsletters()

        await disconnect_from_mongo()

    asyncio.run(main())
    print("database.py _ test")
