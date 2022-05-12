from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.collection import Collection

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
    return render_template('view_collection.html', this_collection = collection)