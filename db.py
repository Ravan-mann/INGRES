import os
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

def get_db_connection():
    """
    Establishes a connection to the MongoDB database.
    Returns the database object or None if connection fails.
    """
    # Load environment variables from .env file
    load_dotenv()

    # Get the connection string from environment variables
    mongo_uri = os.getenv("MONGO_URI")

    if not mongo_uri:
        print("Error: MONGO_URI not found in .env file.")
        return None

    try:
        # Create a new client and connect to the server
        client = MongoClient(mongo_uri)
        
        # Send a ping to confirm a successful connection
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
        
        # Get the default database specified in the URI
        db = client.get_default_database()
        return db

    except ConnectionFailure as e:
        print(f"Could not connect to MongoDB: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example of how to use the connection
if __name__ == "__main__":
    db = get_db_connection()

    if db:
        try:
            # 1. Create: Insert a document into a 'users' collection
            users_collection = db.users
            result = users_collection.insert_one({"name": "Jane Doe", "email": "jane.doe@example.com"})
            print(f"Inserted a document with id: {result.inserted_id}")

            # 2. Read: Find the document
            found_user = users_collection.find_one({"name": "Jane Doe"})
            print(f"Found user: {found_user}")

            # 3. Update: Change a field in the document
            users_collection.update_one({"name": "Jane Doe"}, {"$set": {"email": "jane.d@example.com"}})
            updated_user = users_collection.find_one({"name": "Jane Doe"})
            print(f"Updated user: {updated_user}")

            # 4. Delete: Remove the document
            users_collection.delete_one({"name": "Jane Doe"})
            print("User deleted successfully.")

        except Exception as e:
            print(f"An error occurred during database operation: {e}")
        finally:
            # Close the connection when the app is done
            db.client.close()
            print("MongoDB connection closed.")