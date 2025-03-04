from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from src.models.formio.form import FormModel  # Import your MongoDB models
from src.config.settings import settings


async def init_db():
    """Initialize Beanie with document models."""
    client = AsyncIOMotorClient(settings.MONGO_URI)
    mongo_db = client[settings.MONGO_DATABASE]
    await init_beanie(database=mongo_db, document_models=[FormModel])
