from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# this allows us to define out table and table columns
metadata = MetaData()

# create flask sqlalchemy extension and link it to sqlalchemy
db = SQLAlchemy(metadata = metadata)

"""
-> Must have the __tablename__ property
-> Must have at least one column (attribute)
-> Must inherit from db.Model
"""

class Menu(db.Model, SerializerMixin):
    __tablename__ = "menus"

    # table columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
    price = db.Column(db.Integer)

    # serializer rules (negates)
    serialize_rules = ('-price',)

    # select specific fields
    serialize_only = ('name',)

class Category(db.Model, SerializerMixin):
    __tablename__ = "categories"

    # table columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)
