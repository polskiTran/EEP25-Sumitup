import logging
from pprint import pprint  # noqa: F401

import chromadb
import chromadb.utils.embedding_functions as embedding_functions
from config import settings
from database.database import close_mongo_connection, connect_to_mongo, get_newsletters

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
# ChromaDB Client
# ------------------------------
client = chromadb.CloudClient(
    api_key=settings.chromadb_api_key,
    tenant=settings.chromadb_tenant,
    database=settings.chromadb_database,
)
# create collection if it doesn't exist
try:
    collection = client.get_collection(name=settings.chromadb_collection_name)
except Exception as e:
    logger.error(f"Error getting collection: {e}. Creating collection...")
    collection = client.create_collection(
        name=settings.chromadb_collection_name,
        embedding_function=embedding_functions.GoogleGenerativeAiEmbeddingFunction(
            api_key=settings.google_gemini_genai_api_token,
            model_name=settings.google_gemini_embedding_model,
        ),
    )


# ------------------------------
# Main
# ------------------------------
async def main():
    """
    Add newsletters from mongo db to chromadb collection
    """
    # get newsletters from mongo db
    newsletters = await get_newsletters()
    logger.info(f"Total newsletters: {len(newsletters)}")
    # add documents to collection
    collection = client.get_collection(name=settings.chromadb_collection_name)
    for index, newsletter in enumerate(newsletters):
        logger.info(
            f"Adding {index + 1} out of {len(newsletters)} newsletters ================"
        )
        if collection.get(ids=[newsletter.id])["ids"]:
            logger.info(f"Newsletter already exists: {newsletter.id}")
            continue
        try:
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
        except Exception as e:
            logger.error(f"Error adding newsletter: {e}")


async def date_modify():
    """
    Modify the date format of the newsletters in chromadb collection
    """
    newsletters = await get_newsletters()
    for index, newsletter in enumerate(newsletters):
        logger.info(
            f"Processing {index + 1} out of {len(newsletters)} newsletters ================"
        )
        if collection.get(ids=[newsletter.id])["ids"] == []:
            logger.info(f"Newsletter does not exist: {newsletter.id}")
            continue
        try:
            collection.update(
                ids=[newsletter.id],
                documents=[newsletter.cleaned_md],
                metadatas=[{"date": newsletter.received_datetime.strftime("%Y-%m-%d")}],
            )
        except Exception as e:
            logger.error(f"Error updating newsletter: {e}")


if __name__ == "__main__":
    import asyncio

    async def run():
        # connect to mongo db
        await connect_to_mongo()

        # add documents to collection
        await main()
        # result = collection.query(query_texts=["OpenAI Court order"])
        # pprint(result["metadatas"])
        # await date_modify()

        # disconnect from mongo db
        await close_mongo_connection()

    asyncio.run(run())
