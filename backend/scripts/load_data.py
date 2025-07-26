import pandas as pd
from pymongo import MongoClient
import sys
import os

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
DB_NAME = 'ecommerce_db'

FILES_TO_INGEST= [

    'users.csv',
    'products.csv',
    'orders.csv',
    'order_items.csv',
    'inventory_items.csv',
    'distribution_centers.csv'
]

def ingest_data():
    print(f"Attempting to connect to MongoDB at {MONGO_HOST}:{MONGO_PORT}...")
    try:
        client = MongoClient(MONGO_HOST, MONGO_PORT)
        db = client[DB_NAME]
        print(f"Connected to database: {DB_NAME}")
    except Exception as e:
        print(f"Failed to connect to MongoDB: {e}")
        return
    for file_name in FILES_TO_INGEST:
        try:
            base_dir= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            csv_path = os.path.join(base_dir, 'data', file_name)
        except NameError:
            csv_path = os.path.join('data', file_name)

        collection_name = file_name.split('.')[0]
        collection=db[collection_name  ]
        print(f"\n --- Processing '{file_name}'---")
        try:
            df= pd.read_csv(csv_path)
            print(f"Read {len(df)} rows from {file_name}.")
        except FileNotFoundError:
            print(f"File not found: {csv_path}")
            continue
        except Exception as e:
            print(f"Error reading {csv_path}: {e}")
            continue
        print(f"Clearing Old data from collection '{collection_name}'...")
        collection.delete_many({})
        records = df.to_dict(orient='records')
        if records:
            print(f"Inserting {len(records)} records into collection '{collection_name}'...")
            collection.insert_many(records)
            print(f"Successfully inserted {len(records)} records into '{collection_name}'.")
        else:
            print(f"Error inserting records into '{collection_name}': {e}")
        
        print("\n\n Mile stone 2 complete")
    client.close()

if __name__ == "__main__":
    ingest_data()



