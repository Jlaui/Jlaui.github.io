import os
from dotenv import load_dotenv

# Allows for the storage of sensitive credentials
load_dotenv()


def get_db_config() -> dict:
    # Retrieves MongoDB credentials from environment variables.
    # Raises ValueError if credentials are missing.
    username = os.getenv("MONGO_USERNAME")
    password = os.getenv("MONGO_PASSWORD")

    # Acts as a form of validation; to ensure both the password and username exist
    # Will raise an error is either are missing to prevent a connection without an attempt at
    # inputting valid credentials
    if not username or not password:
        raise ValueError("Missing MongoDB credentials in .env file")

    # Returns credentials as a dictionary for easier use by CRUD
    return {"username": username, "password": password}
