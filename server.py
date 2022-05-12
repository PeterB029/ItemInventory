from flask_app import app
from flask_app.controllers.users import User
from flask_app.controllers.collections import Collection
# from flask_app.controllers.categories import Category
# from flask_app.controllers.items import Item


if __name__ == "__main__":
    app.run(debug=True)