from pymongo import MongoClient

client = MongoClient(
    "mongodb://localhost:27017/"
)

db = client["amazon_customer_support"]

chat_collection = db["chat_history"]

print("MongoDB Connected")