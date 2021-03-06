import re
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.collection import Collection
from flask_app.models.category import Category

@app.route('/collection/new')
def add_collection_page():
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
        return redirect("/")
    return render_template('create_collection.html')

@app.route('/collection/create', methods=['POST'])
def create_collection():
    if not Collection.validate_collection(request.form):
        return redirect('/collection/new')
    data = {
        "title": request.form['title'],
        "description": request.form['description'],
        "image": request.form['image'],
        "user_id": session['user_id']
    }
    Collection.add_collection(data)
    return redirect('/dashboard')

@app.route('/collection/<int:id>')
def collection_page(id):
    data = {
        "id": id
    }
    collection = Collection.get_one_collection(data)
    categories = Category.get_all_categories(data)
    return render_template('view_collection.html', this_collection = collection, all_categories = categories)

@app.route('/collection/edit/<int:id>')
def edit_collection_page(id):
    if 'user_id' not in session:
        flash("You must be logged in to view this page")
        return redirect("/")
    data = {
        "id": id
    }
    collection = Collection.get_one_collection(data)
    return render_template('edit_collection.html', this_collection = collection)


@app.route('/collection/update', methods=['POST'])
def update_collection():
    if not Collection.validate_collection(request.form):
        return redirect('/collection/edit/' + request.form['id']) #CHECK HERE: Does it need to have ID to go back to the edit page.
    data = {
        "id": request.form['id'],
        "description": request.form['description'],
        "title": request.form['title'],
        "image": request.form['image']
    }
    Collection.update_collection(data)
    return redirect('/collection/' + request.form['id'])

@app.route('/collection/delete/<int:id>')
def delete_collection(id):
    data = {
        "id": id
    }
    Collection.delete_collection(data)
    return redirect('/dashboard')
