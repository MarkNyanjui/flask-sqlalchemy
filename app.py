import os
from flask import Flask, request
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_restful import Resource, Api
from flask_cors import CORS

from models import db, Menu, Category
from resources.category import CategoryResource

# import config from .env file
load_dotenv()

# create flask instance
app = Flask(__name__)

# setup cors
CORS(app)

api = Api(app)

# configuring flask through the config object (dict)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
# allow alchemy to display generate sql on the terminal
app.config['SQLALCHEMY_ECHO'] = True

# create the migrate object to manage migrations
migrate = Migrate(app, db)

# link our db to the flask instance
db.init_app(app)

# @app.get('/')
# def index():
#     # route logic
#     return { "message": "Welcome to my restaurant app" }

class Index(Resource):
    # instance method
    def get(self):
        return { "message": "Welcome to my restaurant app" }

@app.get('/menus')
def get_menus():
    menus = Menu.query.all()

    results = []

    for menu in menus:
        results.append(menu.to_dict())

    return results

@app.post('/menus')
def create_menu():
    data = request.json

    # create new instance with the values sent
    menu = Menu(name = data['name'], price = data['price'])

    db.session.add(menu)
    # commit
    db.session.commit()

    print(data)

    return {
        "message": "Menu created successfully",
        "menu": menu.to_dict()
    }

# @app.get('/categories/<id>')
# def get_category(id):
#     category = Category.query.filter_by(id = id).first()

#     if category == None:
#         return { "message": "Category not found" }, 404

#     return category.to_dict(rules=('-menus.category',))


api.add_resource(Index, '/')
"""
The second route is going to facilitate GET(single), PATCH, DELETE
PATCH -> /categories/1
DELETE -> /categories/1
GET one -> /categories/1
"""
api.add_resource(CategoryResource, '/categories', '/categories/<id>')
