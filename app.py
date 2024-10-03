from flask import Flask, request
from flask_migrate import Migrate

from models import db, Menu

# create flask instance
app = Flask(__name__)

# configuring flask through the config object (dict)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurant.db'
# allow alchemy to display generate sql on the terminal
app.config['SQLALCHEMY_ECHO'] = True

# create the migrate object to manage migrations
migrate = Migrate(app, db)

# link our db to the flask instance
db.init_app(app)

@app.get('/')
def index():
    # route logic
    return { "message": "Welcome to my restaurant app" }

@app.get('/menus')
def get_menus():
    menus = Menu.query.all()

    results = []

    for menu in menus:
        results.append(menu.to_json())

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
        "menu": menu.to_json()
    }
