# from pymongo import MongoClient     

# conn = MongoClient()     

# entity = conn.local.users
# users = entity.find()
# print(users)

from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# MongoDB connection
client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB")]  # "script_management_db" will be created when data is inserted

# Collections
users_collection = db['users']  # "users" collection
scripts_collection = db['scripts']  # "scripts" collection
