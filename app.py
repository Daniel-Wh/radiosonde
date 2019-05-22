from flask import Flask
from flask_restful import Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from resources.user_resource import UserRegister


app = Flask(__name__)
app.secret_key = ""
api = Api(app)


jwt = JWT(app, authenticate, identity)  # /auth to check username/password

# @jwt_required for app routes that require auth


@app.route('/')
def hello_world():
    return 'Hello World!'


api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run()
