from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import validators

db = 'item_inventory_schema'

class Item:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['name']
        self.image = data['quantity']
        self.order_link = data['order_link']
        self.notes = data['notes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def add_item_to_collection(cls, data):
        query = "INSERT INTO items (name, quantity, order_link, notes, collection_id) VALUES (%(name)s, %(quantity)s, %(order_link)s, %(notes)s, %(collection_id)s);"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def add_item_to_category(cls, data):
        query = "INSERT INTO items (name, quantity, order_link, notes, category_id) VALUES (%(name)s, %(quantity)s, %(order_link)s, %(notes)s, %(category_id)s);"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_all_items_from_collection(cls, data):
        query = "SELECT * FROM items WHERE collection_id = %(collection_id)s"
        results = connectToMySQL(db).query_db(query)
        return results

    @classmethod
    def get_all_items_from_category(cls, data):
        query = "SELECT * FROM items WHERE category_id = %(catgory_id)s"
        results = connectToMySQL(db).query_db(query)
        return results

    @classmethod
    def get_one_item(cls, data):
        query = "SELECT * from items WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def delete_item(cls, data):
        query = "DELETE FROM items WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @staticmethod
    def validate_item(item):
        is_valid = True
        if len(item['name']) < 3:
            flash("Name must be at least 3 characters long")
            is_valid = False
        if item['quantity'] < 0:
            flash("Quantity must be at least 0")
            is_valid = False
        if not validators.url(item['order_link']):
            flash("URL not invalid. Must be entered as http://[site].[com]")
            is_valid = False
        return is_valid