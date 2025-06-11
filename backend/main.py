from contextlib import asynccontextmanager

from api.newsletters_api import router as newsletters_api
from config import settings
from database.database import close_mongo_connection, connect_to_mongo
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    await connect_to_mongo()
    yield
    # Shutdown
    await close_mongo_connection()


app = FastAPI(lifespan=lifespan)

app.include_router(newsletters_api)


if __name__ == "__main__":
    import uvicorn

    print("Server is running with mongodb connection string: ", settings.mongodb_url)
    uvicorn.run(app, host="0.0.0.0", port=8000)
