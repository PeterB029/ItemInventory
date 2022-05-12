from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'item_inventory_schema'

class Category:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.image = data['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def add_category(cls, data):
        query = "INSERT INTO categories (title, image, collection_id) VALUES (%(title)s, %(image)s, %(collection_id)s);"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_all_categories(cls):
        query = "SELECT * FROM categories"
        results = connectToMySQL(db).query_db(query)
        return results

    @classmethod
    def get_one_category(cls, data):
        query = "SELECT * from categories WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def delete_category(cls, data):
        query = "DELETE FROM categories WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @staticmethod
    def validate_category(category):
        is_valid = True
        if len(category['title']) < 3:
            flash("Title must be at least 3 characters long")
            is_valid = False
        #image validation
        return is_valid