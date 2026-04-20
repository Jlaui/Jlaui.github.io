# services.py
from typing import List, Dict
from crud import AnimalShelter  # Interface to interact with the database
from ranking import rank_animals  # Function used to score and rank animals
import logging

# Initialize logger for this module
logger = logging.getLogger(__name__)


def get_filtered_animals(db: AnimalShelter, category: str) -> List[Dict]:
    try:
        queries = {
            "water": {"breed": {"$in": ["Labrador Retriever", "Chesapeake Bay Retriever", "Newfoundland"]}},
            "mountain": {"breed": {"$in": ["German Shepherd", "Alaskan Malamute", "Old English Sheepdog"]}},
            "disaster": {"breed": {"$in": ["Doberman Pinscher", "German Shepherd", "Golden Retriever"]}},
            "reset": {}
        }

        # Select query for the given category
        query = queries.get(category, {})
        # Fetch records from the database
        records = db.read(query, limit=50)
        if not records:
            return []

        # Convert _id to string and traits list to comma-separated string
        for record in records:
            if "_id" in record:
                record["_id"] = str(record["_id"])
            if "traits" in record and isinstance(record["traits"], list):
                record["traits"] = ", ".join(record["traits"])

        # Rank and sort the animals using scoring function
        return rank_animals(records, category)
    except Exception as e:
        # Log errors during the retrieval or ranking
        logger.error(f"Error retrieving filtered animals: {e}")
        return []
