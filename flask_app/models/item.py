from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'item_inventory_schema'

class Item:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.quantity = data['quantity']
        self.order_link = data['order_link']
        self.notes = data['notes']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def add_item(cls, data):
        query = "INSERT INTO items (name, quantity, order_link, notes, category_id) VALUES (%(name)s, %(quantity)s, %(order_link)s, %(notes)s, %(category_id)s);"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_all_items(cls, data):
        query = "SELECT * FROM items WHERE category_id = %(category_id)s ORDER BY name ASC"
        results = connectToMySQL(db).query_db(query, data)
        return results

    @classmethod
    def get_one_item(cls, data):
        query = "SELECT * from items WHERE id=%(id)s"
        results = connectToMySQL(db).query_db(query, data)
        return cls(results[0])

    @classmethod
    def update_item(cls, data):
        query = "UPDATE items SET name=%(name)s, quantity=%(quantity)s, order_link=%(order_link)s, notes=%(notes)s WHERE id=%(id)s"
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
        if float(item['quantity']) < 0:
            flash("Quantity must be at least 0")
            is_valid = False
        # if not validators.url(item['order_link']):
        #     flash("URL not invalid. Must be entered as http://[site].[com]")
        #     is_valid = False
        return is_valid