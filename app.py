from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from resources.user_resource import UserRegister
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.secret_key = ""
api = Api(app)
db.init_app(app)

jwt = JWT(app, authenticate, identity)  # /auth to check username/password

# @jwt_required for app routes that require auth


@app.route('/')
def hello_world():
    return 'Hello World!'


api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run()
