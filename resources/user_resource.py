from models.user_model import User
from flask_restful import Resource, reqparse
from models.database import DataBase
import sqlite3


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
        if User.find_by_username(data['username']) is None:
            connection = sqlite3.connect(DataBase.db_path)
            cursor = connection.cursor()
            query = "INSERT INTO registeredUsers VALUES (null, ?, ?)"
            cursor.execute(query, (data['username'], data['password']))
        else:
            return {'Message': "Username already exists"}, 400

        connection.commit()
        connection.close()

        return {'message': "user was created successfully"}, 201


