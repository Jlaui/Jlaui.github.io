from pymongo import MongoClient
from typing import List, Dict
from config import get_db_config
import logging

# Configure logging; more detailed information about CRUD operations
# Assists with debugging and the monitoring of the system
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AnimalShelter:
    # CRUD operations for Animal collection in MongoDB

    def __init__(self):
        config = get_db_config()
        username = config["username"]
        password = config["password"]
        host = "localhost"
        port = 27017
        db_name = "aac"
        col_name = "animals"

        # Try connecting to the database
        try:
            self.client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}")
            self.database = self.client[db_name]
            self.collection = self.database[col_name]
            # Create indexes for performance optimization
            self.collection.create_index("breed")
            self.collection.create_index("age_upon_outcome_in_weeks")

            logger.info("Connected to MongoDB successfully.")
        except Exception as e:
            logger.error(f"Error connecting to MongoDB: {e}")
            raise

    # Create method; used for the insertion of a new document
    # In the event it's successful, true is returned, otherwise false is returned
    def create(self, data: Dict) -> bool:
        if not data:
            raise ValueError("Nothing to save, data is empty")

        required_fields = ["breed", "age_upon_outcome_in_weeks"]
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        try:
            result = self.collection.insert_one(data)
            return result.inserted_id is not None
        except Exception as e:
            logger.error(f"Error creating document: {e}")
            return False

    # Read method; queries the collection for documents that match the inputted query
    # Returns a list of dictionaries that represent the documents
    def read(self, query=None, limit=100, skip=0) -> List[Dict]:
        if query is None:
            query = {}
        try:
            cursor = self.collection.find(query).skip(skip).limit(limit)
            return list(cursor)
        except Exception as e:
            logger.error(f"Error reading from database: {e}")
            return []

    # Update method; Updates the documents that match the query
    # Returns the number of documents which are successfully modified
    def update(self, query: Dict, new_values: Dict, multiple: bool = False) -> int:
        try:
            if multiple:
                result = self.collection.update_many(query, new_values)
            else:
                result = self.collection.update_one(query, new_values)
            return result.modified_count
        except Exception as e:
            logger.error(f"Error updating document(s): {e}")
            return 0

    # Delete method; Updates the documents that match the inputted query
    # Returns the number of documents removed.
    def delete(self, query: Dict, multiple: bool = False) -> int:
        try:
            if multiple:
                result = self.collection.delete_many(query)
            else:
                result = self.collection.delete_one(query)
            return result.deleted_count
        except Exception as e:
            logger.error(f"Error deleting document(s): {e}")
            return 0


def get_breed_distribution(self):
    try:
        pipeline = [
            {"$group": {"_id": "$breed", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}}
        ]
        return list(self.collection.aggregate(pipeline))
    except Exception as e:
        logger.error(f"Error in aggregation pipeline: {e}")
        return []
