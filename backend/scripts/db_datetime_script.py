import logging
from datetime import datetime

from config import settings
from database.database import (
    close_mongo_connection,
    connect_to_mongo,
    get_newsletters,
    upsert_newsletter,
)
from helpers.helpers import convert_internal_date_to_datetime
from pymongo import MongoClient

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


async def main():
    """Convert the internal date to a datetime object."""
    newsletters = await get_newsletters()
    total_docs = len(newsletters)
    logger.info(f"Total documents: {total_docs}")

    for index, newsletter in enumerate(newsletters):
        logger.info(
            f"Processing {index + 1} out of {total_docs} documents ================"
        )
        if newsletter.received_datetime is None:
            new_date: datetime = convert_internal_date_to_datetime(
                newsletter.internal_date
            )
            logger.info(
                f"Newsletter: {newsletter.id} - {newsletter.internal_date} -> {new_date}"
            )
            # update the newsletter
            try:
                newsletter.received_datetime = new_date
                await upsert_newsletter(newsletter)
                logger.info(f"Updated newsletter: {newsletter.id}")
            except Exception as e:
                logger.error(f"Error updating newsletter: {e}")
        else:
            logger.info(f"Skipping newsletter: {newsletter.id} - already processed")


async def remove_received_datetime():
    """Remove the received datetime from the newsletter."""
    client = MongoClient(settings.mongodb_url)
    db = client[settings.database_name]
    collection = db[settings.newsletter_collection_name]
    result = collection.update_many(
        {},  # empty filter = all documents
        {"$unset": {"received_datetime": ""}},
    )
    logger.info(f"Modified {result.modified_count} documents.")


if __name__ == "__main__":
    import asyncio

    # connect to db
    async def run():
        await connect_to_mongo()

        await main()
        # await remove_received_datetime()

        # close db connection
        await close_mongo_connection()

    asyncio.run(run())
