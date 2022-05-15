from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.item import Item

#opens the add item to category page
@app.route('/<int:collectionID>/<int:categoryID>/item/new')
def add_item(collectionID, categoryID):
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
    return render_template('create_item.html', this_collectionID = collectionID, this_categoryID = categoryID)

#calls the class query method to CREATE new item in category
@app.route('/item/create', methods=['POST'])
def create_item_category():
    if not Item.validate_item(request.form):
        return redirect(f"/{request.form['collection_id']}/{request.form['category_id']}/item/new")
    data = {
        "name": request.form['name'],
        "quantity": request.form['quantity'],
        "order_link": request.form['order_link'],
        "notes": request.form['notes'],
        "category_id": request.form['category_id']
    }
    Item.add_item(data)
    return redirect(f"/{request.form['collection_id']}/category/{request.form['category_id']}")

#opens the item READ page
@app.route('/<int:collectionID>/<int:categoryID>/item/<int:id>')
def item_page(collectionID, categoryID, id):
    data = {
        "id": id
    }
    item = Item.get_one_item(data)
    return render_template('view_item.html', this_collectionID = collectionID, this_categoryID = categoryID, this_item = item)

#opens the edit item page (if from categories page)
@app.route('/<int:collectionID>/<int:categoryID>/item/edit/<int:id>')
def edit_item_page(collectionID, categoryID, id):
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
        return redirect("/")
    data = {
        "id": id
    }
    item = Item.get_one_item(data)
    return render_template('edit_item.html', this_item = item, this_collectionID = collectionID, this_categoryID = categoryID)

#calls the class query method to UPDATE the item
@app.route('/item/update', methods=['POST'])
def update_item():
    if not Item.validate_item(request.form):
        return redirect(f"/{request.form['collection_id']}/{request.form['category_id']}/item/edit/{request.form['id']}")
    data = {
        "id": request.form['id'],
        "name": request.form['name'],
        "quantity": request.form['quantity'],
        "order_link": request.form['order_link'],
        "notes": request.form['notes'],
        "category_id": request.form['category_id']
    }
    Item.update_item(data)
    return redirect(f"/{request.form['collection_id']}/{request.form['category_id']}/item/{request.form['id']}")

#calls the class query method to DELETE item
@app.route('/<int:collectionID>/<int:categoryID>/item/delete/<int:id>')
def delete_item(collectionID, categoryID, id):
    data = {
        "id": id
    }
    Item.delete_item(data)
    return redirect(f"/{str(collectionID)}/category/{str(categoryID)}")
