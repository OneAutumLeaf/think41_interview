from pymongo import MongoClient

MONGO_CONNECTION_STRING = "mongodb://localhost:27017/"
DB_NAME ="ecommerce_db"

try:
    client = MongoClient(MONGO_CONNECTION_STRING)
    db = client[DB_NAME]
    print(f"Connected to MongoDB database: {DB_NAME}")
except Exception as e:
    print(f"Failed to connect to MongoDB: {e}")
    db = None