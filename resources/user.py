from flask_restful import Resource, reqparse
from flask_bcrypt import generate_password_hash, check_password_hash
from models import User, db

class UserResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', required=True, help='Name is required')
    parser.add_argument('phone', required=True, help="Phone number is required")
    parser.add_argument('password', required=True, help="Password is required")

    # create user method
    def post(self):
        data = self.parser.parse_args()
        print(data)

        # 1. Verify phone is unique
        phone = User.query.filter_by(phone = data['phone']).first()

        if phone:
            return {
                "message": "Phone number already taken"
            }, 422

        # 2. Encrypt our password
        hash = generate_password_hash(data['password']).decode('utf-8')

        # 3. Save the user to the db
        user = User(name=data['name'], phone=data['phone'], password = hash)

        db.session.add(user)

        db.session.commit()

        # 4. generate jwt and send it to react

        return {
            "message": "User created successfully",
            "user": user.to_dict()
        }

class LoginResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('phone', required=True, help="Phone number is required")
    parser.add_argument('password', required=True, help="Password is required")

    def post(self):
        data = self.parser.parse_args()

        # 1. retrieve the user using the unique field
        user = User.query.filter_by(phone = data['phone']).first()

        if user == None:
            return {
                "message": "Invalid phone number/password"
            }, 401

        # if password matches, everything is ok
        if check_password_hash(user.password, data['password']):
            # generate jwt
            return {
                "message": "Login successful",
                "user": user.to_dict()
            }
        else:
            return {
                "message": "Invalid phone number/password"
            }, 401
