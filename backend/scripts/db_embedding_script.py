import logging

from config import settings
from database.database import (
    close_mongo_connection,
    connect_to_mongo,
    get_newsletters,
    upsert_newsletter,
)
from helpers.helpers import convert_internal_date_to_datetime
from pymongo.errors import PyMongoError
from services.genai_service import embed_newsletter

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
# Function to add embeddings to collection
# ------------------------------
async def newsletter_embedding_test():
    """Test the embedding function."""
    # get newsletters
    newsletters = await get_newsletters()
    total_docs = len(newsletters)
    logger.info(f"Total documents: {total_docs}")
    # get first newsletter
    newsletter = newsletters[0]
    logger.info(f"Newsletter: {newsletter.subject}")
    # get cleaned_md
    cleaned_md = newsletter.cleaned_md
    # generate embedding
    embeddings = embed_newsletter(cleaned_md)
    logger.info(f"Embedding:<{embeddings}>")


async def embedding_test():
    """Test the embedding function."""
    query = "Figma news"
    embedding = embed_newsletter(query)
    logger.info(f"Embedding:<{embedding}>")


async def add_embeddings_to_collection():
    """Add embeddings to the collection."""
    try:
        # get newsletters
        newsletters = await get_newsletters()
        total_docs = len(newsletters)
        logger.info(f"(*) Total newsletters to process: {total_docs}")

        for index, newsletter in enumerate(newsletters):
            logger.info(
                f"\n(*) Processing {index + 1} out of {total_docs} documents ============"
            )
            cleaned_md = newsletter.cleaned_md

            # check if embedding already exists
            if newsletter.cleaned_md_embedding is not None:
                logger.info(
                    f"Skipping document {newsletter.id}: Embedding already exists"
                )
                continue

            if not cleaned_md:
                logger.error(
                    f"Skipping document {newsletter.id}: No cleaned_md content"
                )
                continue

            # Generate embedding
            logger.info(
                f"Embedding newsletter: {newsletter.id} of date: {convert_internal_date_to_datetime(newsletter.internal_date).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embedding = embed_newsletter(cleaned_md)
            if embedding is None:
                logger.error(
                    f"Failed to generate embedding for document {newsletter.id}"
                )
                break

            # Update document with embedding
            try:
                newsletter.cleaned_md_embedding = embedding
                await upsert_newsletter(newsletter)
                logger.info(
                    f"Updated document {newsletter.id} with embedding ({index + 1}/{total_docs})"
                )
            except PyMongoError as e:
                logger.error(f"Error updating document {newsletter.id}: {e}")
                continue

        logger.info("(*) Done processing all newsletters")
    except PyMongoError as e:
        logger.error(f"MongoDB error: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")


# Run the script
if __name__ == "__main__":
    # Connect to MongoDB
    import asyncio

    async def run():
        # connect to db
        await connect_to_mongo()

        # add embeddings to collection
        # await add_embeddings_to_collection()

        # test embedding
        await embedding_test()

        # disconnect from db
        await close_mongo_connection()

    asyncio.run(run())
