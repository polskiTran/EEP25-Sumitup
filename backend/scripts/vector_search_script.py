from datetime import datetime

import chromadb
from config import settings
from database.database import connect_to_mongo, disconnect_from_mongo, get_collection
from services.genai_service import embed_newsletter


async def mongodb_vector_search(
    query: str, limit: int = 5, pre_filter_query: dict = {}
):
    """
    Search for newsletters in mongodb using vector search
    Args:
        query (str): The query to search for
        limit (int): The number of results to return
        pre_filter_query (dict): The pre filter query to apply to the search
    Returns:
        list[dict]: The list of results
    """

    # connect to mongo db
    await connect_to_mongo()
    collection = get_collection("newsletters")

    print(pre_filter_query)

    # vector search
    query_vector = embed_newsletter(query)
    cursor = collection.aggregate(
        [
            {
                "$vectorSearch": {
                    "queryVector": query_vector,
                    "path": "cleaned_md_embedding",
                    "numCandidates": 100,
                    "limit": limit,
                    "index": "vector_index",
                    "filter": pre_filter_query,
                }
            }
        ]
    )

    # clean results
    cleaned_results = []
    async for doc in cursor:
        cleaned_results.append(
            {
                "id": doc["_id"],
                "sender_name": doc["sender_name"],
                "sender_email": doc["sender_email"],
                "subject": doc["subject"],
                "received_datetime": doc["received_datetime"],
                # "received_datetime": doc["received_datetime"],
                # "cleaned_md": doc["cleaned_md"],
            }
        )
    # disconnect from mongo db
    await disconnect_from_mongo()
    return cleaned_results


async def chromadb_vector_search(query: str, limit: int = 5, filter: dict = {}):
    """
    Search for newsletters in chromadb using vector search
    Args:
        query (str): The query to search for
        limit (int): The number of results to return
        filter (dict): The filter to apply to the search
    Returns:
        list[dict]: The list of results
    """
    # connect to chromadb
    client = chromadb.CloudClient(
        api_key=settings.chromadb_api_key,
        tenant=settings.chromadb_tenant,
        database=settings.chromadb_database,
    )
    try:
        collection = client.get_collection(name=settings.chromadb_collection_name)
    except Exception as e:
        print(f"Error getting collection: {e}.")
    result = collection.query(query_texts=[query], where=filter, n_results=limit)
    return result["metadatas"]


# async def chroma_prefilter_vector_search(query: str, limit: int = 5, pre-filter: dict = {}):
#     """
#     Search for newsletters in chromadb using vector search with prefilter
#     Args:
#         query (str): The query to search for
#         limit (int): The number of results to return
#         filter (dict): The filter to apply to the search
#     Returns:
#         list[dict]: The list of results
#     """
#     # connect to chromadb
#     client = chromadb.CloudClient(
#         api_key=settings.chromadb_api_key,
#         tenant=settings.chromadb_tenant,
#         database=settings.chromadb_database,
# 	)
#     try:
#         collection = client.get_collection(name=settings.chromadb_collection_name)
#     except Exception as e:
#         print(f"Error getting collection: {e}.")
#     base_retrieval = collection.as_retriever(
# 		search_kwargs={
# 			"query": query,
# 			"where": pre_filter,
# 			"n_results": limit,
# 		}
# 	)
#     pass

if __name__ == "__main__":
    import asyncio
    from pprint import pprint

    # test data
    date1 = "2025-07-10"
    date2 = "2025-07-13"
    date_timestamp1 = int(datetime.strptime(date1, "%Y-%m-%d").timestamp() * 1000)
    date_timestamp2 = int(datetime.strptime(date2, "%Y-%m-%d").timestamp() * 1000)

    # query
    query = "foldables"
    limit = 5
    # pre filter query
    # pre_filter_query = {
    #     "internal_date": {
    #         "$gte": date_timestamp1,
    #         "$lt": date_timestamp2,
    #     }
    # }
    pre_filter_query = {"date": "2025-07-14"}
    # chroma_filter = {
    #     "date_timestamp": {
    #         "$gte": int(datetime.strptime(date1, "%Y-%m-%d").timestamp())
    #     }
    # }
    # chroma_filter = {
    #     "$and": [
    #         {"date": "2025-07-06"},
    #         {"date": "2025-07-07"},
    #         {"date": "2025-07-08"},
    #         {"date": "2025-07-09"},
    #         {"date": "2025-07-10"},
    #         {"date": "2025-07-11"},
    #         {"date": "2025-07-12"},
    #     ]
    # }
    chroma_filter = {"$eq": {"date": "2025-07-14"}}

    async def run():
        print("---------------------------------------------------")
        print("---------------------------------------------------")
        print("mongodb_vector_search")
        pprint(await mongodb_vector_search(query, limit, pre_filter_query))
        print("---------------------------------------------------")
        print("---------------------------------------------------")
        print("chromadb_vector_search")
        pprint(await chromadb_vector_search(query, limit, chroma_filter))

    asyncio.run(run())
