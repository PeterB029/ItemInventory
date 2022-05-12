from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'item_inventory_schema'

class Collection:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.image = data['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def add_collection(cls, data):
        query = "INSERT INTO collections (title, image, user_id) VALUES (%(title)s, %(image)s, %(user_id)s);"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_all_collections(cls):
        query = "SELECT * FROM collections"
        results = connectToMySQL(db).query_db(query)
        return results

    @classmethod
    def get_one_collection(cls, data):
        query = "SELECT * from collections WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update_collection(cls, data):
        query = "UPDATE collections SET title=%(title)s, image=%(image)s WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def delete_collection(cls, data):
        query = "DELETE FROM collections WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @staticmethod
    def validate_collection(collection):
        is_valid = True
        if len(collection['title']) < 3:
            flash("Title must be at least 3 characters long")
            is_valid = False
        #image validation
        return is_valid