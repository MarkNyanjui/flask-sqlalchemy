from flask_restful import Resource, reqparse
from flask import request
from flask_jwt_extended import jwt_required
from models import Category, db

class CategoryResource(Resource):
    # create new instance of reqparser
    # this a class attribute
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True, help="Category name is required")

    # /categories?page=1&take=100
    # /categories/<id>
    @jwt_required()
    def get(self, id = None):
        # means retrieve all categories

        if id == None:
            results = []

            print(request.args)

            # categories = Category.query.paginate(page = int(request.args.get('page')), per_page= int(request.args.get('take')))
            categories = Category.query.all()

            # print(categories)

            for category in categories:
                results.append(category.to_dict())

            # return {
            #     "total": categories.total,
            #     "items": results,
            #     "page": categories.page
            # }
            return results

        category = Category.query.filter_by(id = id).first()

        if category == None:
            return { "message": "Category not found" }, 404

        return category.to_dict()

    def post(self):
        data = self.parser.parse_args()

        # kwargs
        category = Category(**data)

        db.session.add(category)

        db.session.commit()

        return {
            "message": "Category created successfuly",
            "category": category.to_dict()
            }, 201

    def patch(self, id):
        data = self.parser.parse_args()

        # retrieve the record
        category = Category.query.filter_by(id = id).first()

        # if category doesn`t exist, we return an error
        if category == None:
            return { "message": "Category not found" }, 404

        category.name = data['name']

        db.session.commit()

        return {
            "message": "Category updated successfully",
            "category": category.to_dict()
        }

    def delete(self, id):
        # retrieve the record
        category = Category.query.filter_by(id = id).first()

        # if category doesn`t exist, we return an error
        if category == None:
            return { "message": "Category not found" }, 404

        db.session.delete(category)

        db.session.commit()

        return { "message": "Category deleted successfully" }
