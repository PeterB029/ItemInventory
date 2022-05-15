from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.category import Category
from flask_app.models.item import Item

#Opens the create category page
@app.route('/<int:collectionID>/category/new')
def add_category_page(collectionID):
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
        return redirect('/')
    return render_template('create_category.html', this_collectionID = collectionID)
    #We are passing in the collectionID so we can make a hidden field called collection_id to pass in 
    #when creating the category under collection.

#calls class quert methods to CREATE new category
@app.route('/category/create', methods=['POST'])
def create_category():
    if not Category.validate_category(request.form):
        return redirect('/' + request.form['collection_id'] + '/category/new')
    data = {
        "title": request.form['title'],
        "image": request.form['image'],
        "collection_id": request.form['collection_id']
    }
    Category.add_category(data)
    return redirect("/collection/" + request.form['collection_id'])
    #Go back to the Collection the Category is under.

#opens the READ category page
@app.route('/<int:collectionID>/category/<int:id>')
def category_page(collectionID, id):
    data = {
        "id": id
    }
    dataItem = {
        "category_id": id
    }
    category = Category.get_one_category(data)
    items = Item.get_all_items(dataItem)
    return render_template('view_category.html', this_category = category, all_items = items, this_collectionID = collectionID)

    #opens the edit category page
@app.route('/<int:collectionID>/category/edit/<int:id>')
def edit_category_page(collectionID, id):
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
        return redirect("/")
    data = {
        "id": id
    }
    category = Category.get_one_category(data)
    return render_template('edit_category.html', this_category = category, this_collectionID = collectionID)

#calls class query method to UPDATE category data
@app.route('/category/update', methods=['POST'])
def update_category():
    if not Category.validate_category(request.form):
        return redirect('/' + request.form['collection_id'] + '/category/edit/' + request.form['id'])
    data = {
        "id": request.form['id'],
        "title": request.form['title'],
        "image": request.form['image']
    }
    Category.update_category(data)
    return redirect('/' + request.form['collection_id'] + '/category/' + request.form['id'])

#calls class query method to DELETE category data
@app.route('/<int:collectionID>/category/delete/<int:id>')
def delete_category(collectionID, id):
    data = {
        "id": id
    }
    Category.delete_category(data)
    return redirect('/collection/' + str(collectionID))
