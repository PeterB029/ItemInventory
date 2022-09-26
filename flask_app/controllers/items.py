from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.item import Item

#opens the add item to category page
@app.route('/collection/<int:collectionID>/category/<int:categoryID>/item/new')
def add_item(collectionID, categoryID):
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
    return render_template('create_item.html', collectionID, categoryID)

#calls the class query method to CREATE new item in category
@app.route('<int:collectionID>/<int:categoryID>/item/create', methods=['POST'])
def create_item_category(collectionID, categoryID):
    if not Item.validate_item(request.form):
        return redirect(f"/{collectionID}/{categoryID}/item/new")
    data = {
        "name": request.form['name'],
        "quantity": request.form['quantity'],
        "order_link": request.form['order_link'],
        "notes": request.form['notes'],
        "category_id": categoryID
    }
    Item.add_item(data)
    return redirect(f"/collection/{collectionID}/category/{categoryID}")

#opens the item READ page
@app.route('/collection/<int:collectionID>/category/<int:categoryID>/item/<int:id>')
def item_page(collectionID, categoryID, id):
    data = {
        "id": id
    }
    this_item = Item.get_one_item(data)
    return render_template('view_item.html', collectionID, categoryID, this_item)

#opens the edit item page (if from categories page)
@app.route('/collection/<int:collectionID>/category/<int:categoryID>/item/edit/<int:id>')
def edit_item_page(collectionID, categoryID, id):
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
        return redirect("/")
    data = {
        "id": id
    }
    this_item = Item.get_one_item(data)
    return render_template('edit_item.html', this_item, collectionID, categoryID)

#calls the class query method to UPDATE the item
@app.route('/<int:collectionID>/<int:categoryID>/item/update/<int:id>', methods=['POST'])
def update_item(collectionID, categoryID, id):
    if not Item.validate_item(request.form):
        return redirect(f"/collection/{collectionID}/category/{categoryID}/item/edit/{id}")
    data = {
        "id": request.form['id'],
        "name": request.form['name'],
        "quantity": request.form['quantity'],
        "order_link": request.form['order_link'],
        "notes": request.form['notes'],
        "category_id": categoryID
    }
    Item.update_item(data)
    return redirect(f"/collection/{collectionID}/category/{categoryID}/item/{id}")

#calls the class query method to DELETE item
@app.route('/<int:collectionID>/<int:categoryID>/item/delete/<int:id>')
def delete_item(collectionID, categoryID, id):
    data = {
        "id": id
    }
    Item.delete_item(data)
    return redirect(f"/collection/{collectionID}/category/{categoryID}")