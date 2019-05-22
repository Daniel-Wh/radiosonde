from models.user_model import UserModel
from flask_restful import Resource, reqparse


class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank")

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']) is None:
            user = UserModel(**data)
            user.save_to_db()
        else:
            return {'Message': "Username already exists"}, 400

        return {'message': "user was created successfully"}, 201


