from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'item_inventory_schema'

class Category:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.image = data['image']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def add_category(cls, data):
        query = "INSERT INTO categories (title, description, image, collection_id) VALUES (%(title)s, %(description)s, %(image)s, %(collection_id)s);"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_all_categories(cls, data):
        query = "SELECT * FROM categories WHERE collection_id=%(id)s ORDER BY title ASC"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_one_category(cls, data):
        query = "SELECT * from categories WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update_category(cls, data):
        query = "UPDATE categories SET title=%(title)s, description=%(description)s, image=%(image)s WHERE id=%(id)s"
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