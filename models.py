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
    name = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=True, default=0)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    created_at = db.Column(db.TIMESTAMP)

    #defining many to one
    category = db.relationship("Category", back_populates="menus")
    # serializer rules (negates)
    serialize_rules = ('-category.menus', '-category_id')

    # select specific fields
    # serialize_only = ('name',)

class Category(db.Model, SerializerMixin):
    __tablename__ = "categories"

    # table columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text)

    # define one to many
    menus = db.relationship("Menu", back_populates="category")

    serialize_rules = ('-menus',)

class User(db.Model, SerializerMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable=False)
    phone = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    # never send password back to client
    serialize_rules = ('-password',)
