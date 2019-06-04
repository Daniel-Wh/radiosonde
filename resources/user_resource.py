from models.user_model import UserModel
from flask_restful import Resource, reqparse


# class that registers users with their username and password and saves them to the database
class UserRegister(Resource):
    # this parser makes sure that it has received a string for both username and password
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank")

    # Creates new user and saves username and password to database or gives message that the username exists already
    def post(self):
        data = UserRegister.parser.parse_args()
        # is the username does not exist create new user, else give error message
        if UserModel.find_by_username(data['username']) is None:
            user = UserModel(**data)  # creates user with data that was entered by the user
            user.save_to_db()
        else:
            return {'Message': "Username already exists"}, 400

        # message to let user know they can now login using the username and password they provided
        return {'message': "user was created successfully"}, 201


