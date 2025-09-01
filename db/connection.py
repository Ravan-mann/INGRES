from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create/get a database
db = client["mydatabase"]

# Create/get a collection
collection = db["users"]

# Insert a document
user = {"name": "Ravan", "age": 22, "city": "Delhi"}
collection.insert_one(user)

# Find a document
result = collection.find_one({"name": "Ravan"})
print(result)
