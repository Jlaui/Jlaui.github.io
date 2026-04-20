# Example Python Code to Insert a Document 

from pymongo import MongoClient 
from bson.objectid import ObjectId 

class AnimalShelter(object): 
    """ CRUD operations for Animal collection in MongoDB """ 

    def __init__(self, username, password): 
        self.username = username
        self.password = password
        # Initializing the MongoClient. This helps to access the MongoDB 
        # databases and collections. This is hard-wired to use the aac 
        # database, the animals collection, and the aac user. 
        # 
        # You must edit the password below for your environment. 
        # 
        # Connection Variables 
        # 
        USER = self.username
        PASS = self.password 
        HOST = 'localhost' 
        PORT = 27017 
        DB = 'aac' 
        COL = 'animals' 
        # 
        # Initialize Connection 
        # 
        self.client = MongoClient(f'mongodb://{username}:{password}@localhost:27017')
        self.database = self.client['%s' % (DB)] 
        self.collection = self.database['%s' % (COL)] 

    # Create a method to return the next available record number for use in the create method
            
    # Complete this create method to implement the C in CRUD. 
    def create(self, data):
        if data:  # Ensure data is not empty
            result = self.collection.insert_one(data)  # Inserts the document
            return True if result.inserted_id else False  # Checks success
        else:
            raise ValueError("Nothing to save, data parameter is empty")
        
    # Create method to implement the R in CRUD.
    
    def read(self, query):
        try:
            documents = list(self.collection.find(query))  # Executes the query
            return documents if documents else []  # Returns a list of the results
        except Exception as e:
            print(f"Error reading from database: {e}")
            return []
        
    #Creates method to implement the U in CRUD.
    #This is used for updating documents that match the query 
    
    def update(self, query, new_values, multiple=False):
        
        try:
            if multiple:
                result = self.collection.update_many(query, new_values)
            else:
                result = self.collection.update_one(query, new_values)
            return result.modified_count
        
        except Exception as e:
            print(f"Error updating document(s): {e}")
            return 0
        
    #Creates method to implement the D in CRUD
    #This is used for deleting documents that match the query
    
    def delete(self,query, multiple=False):
        
        try:
            if multiple:
                result = self.collection.delete_many(query)
            else:
                result = self.collection.delete_one(query)
            return result.deleted_count
        
        except Exception as e:
            print(f"Error deleting document(s): {e}")
            return 0