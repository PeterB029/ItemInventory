from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.category import Category
from flask_app.models.item import Item

#Opens the create category page
@app.route('/collection/<int:collectionID>/category/new')
def add_category_page(collectionID):
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
        return redirect('/')
    return render_template('create_category.html', collectionID)

#calls class quert methods to CREATE new category
@app.route('/<int:collectionID>/category/create', methods=['POST'])
def create_category(collectionID):
    if not Category.validate_category(request.form):
        return redirect(f'/collection/{collectionID}/category/new')
    data = {
        "title": request.form['title'],
        "description": request.form['description'],
        "image": request.form['image'],
        "collection_id": request.form['collection_id']
    }
    Category.add_category(data)
    return redirect(f'/collection/{collectionID}')
    #Go back to the Collection the Category is under.

#opens the READ category page
@app.route('/collection/<int:collectionID>/category/<int:id>')
def category_page(collectionID, id):
    data = {
        "id": id
    }
    dataItem = {
        "category_id": id
    }
    this_category = Category.get_one_category(data)
    all_items = Item.get_all_items(dataItem)
    return render_template('view_category.html', this_category, all_items, collectionID)

    #opens the edit category page
@app.route('/collection/<int:collectionID>/category/edit/<int:id>')
def edit_category_page(collectionID, id):
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
        return redirect("/")
    data = {
        "id": id
    }
    this_category = Category.get_one_category(data)
    return render_template('edit_category.html', this_category, collectionID)

#calls class query method to UPDATE category data
@app.route('/<int:collectionID>/category/update/<int:id>', methods=['POST'])
def update_category(collectionID, id):
    if not Category.validate_category(request.form):
        return redirect(f'/{collectionID}/category/edit/{id}' )
    data = {
        "id": id,
        "title": request.form['title'],
        "description": request.form['description'],
        "image": request.form['image']
    }
    Category.update_category(data)
    return redirect(f'/collection/{collectionID}/category/{id}')

#calls class query method to DELETE category data
@app.route('/<int:collectionID>/category/delete/<int:id>')
def delete_category(collectionID, id):
    data = {
        "id": id
    }
    Category.delete_category(data)
    return redirect(f'/collection/{collectionID}')
