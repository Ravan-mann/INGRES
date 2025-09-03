import os
import pandas as pd
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

# --- Database Connection ---

def get_db_connection():
    """
    Establishes a connection to the MongoDB database.
    Returns the database object or None if connection fails.
    """
    load_dotenv()
    mongo_uri = os.getenv("MONGO_URI")

    if not mongo_uri:
        print("Error: MONGO_URI not found in .env file.")
        return None

    try:
        client = MongoClient(mongo_uri, serverSelectionTimeoutMS=5000)
        # The ismaster command is cheap and does not require auth.
        client.admin.command('ismaster')
        print("Successfully connected to MongoDB!")
        db = client.get_default_database()
        return db
    except ConnectionFailure as e:
        print(f"Could not connect to MongoDB: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# --- Data Loading Script ---

def load_csv_to_mongo(csv_path="data/final_nhs-wq_pre_2022_compressed.csv", collection_name="water_quality"):
    """
    Loads data from the specified CSV file into a MongoDB collection.
    This function will drop the existing collection to prevent duplicates.
    """
    db = get_db_connection()
    if not db:
        return

    try:
        # Drop the collection if it exists to ensure a fresh import
        if collection_name in db.list_collection_names():
            print(f"Dropping existing collection: '{collection_name}'")
            db[collection_name].drop()

        print(f"Reading data from {csv_path}...")
        df = pd.read_csv(csv_path, na_values=['#VALUE!'])
        df.columns = [col.strip() for col in df.columns]
        data = df.to_dict(orient='records')

        print(f"Inserting {len(data)} records into '{collection_name}' collection...")
        db[collection_name].insert_many(data)
        print("Data loaded successfully into MongoDB.")

    except FileNotFoundError:
        print(f"Error: The file was not found at {csv_path}")
    except Exception as e:
        print(f"An error occurred during data loading: {e}")

if __name__ == "__main__":
    print("Running database setup to load CSV data into MongoDB...")
    load_csv_to_mongo()