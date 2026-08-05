import os
from pymongo import MongoClient

MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI not found in environment variables.")

client = MongoClient(MONGODB_URI)

db = client["amazon_customer_support"]

chat_collection = db["chat_history"]

print("✅ MongoDB Connected")