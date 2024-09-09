# from pymongo import MongoClient     

# conn = MongoClient()     

# entity = conn.local.users
# users = entity.find()
# print(users)

from pymongo import MongoClient
from dotenv import load_dotenv
import os
import logging

# Load environment variables from .env file
load_dotenv()

# Setup logging to monitor issues
logging.basicConfig(level=logging.INFO)

try:
    client = MongoClient(os.getenv("MONGO_URI"))
    db = client[os.getenv("MONGO_DB")]
    logging.info("Successfully connected to MongoDB")
except Exception as e:
    logging.error(f"Error connecting to MongoDB: {e}")
    raise
