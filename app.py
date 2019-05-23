from flask import Flask, render_template
from flask_restful import Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from resources.user_resource import UserRegister
from db import db

uri = "postgres://keujsruvqpelne:291827d8388be8155c772e76b509b9f4ef0e9e81b2aef479644628d60aa11c9b@ec2-" \
      "54-83-205-27.compute-1.amazonaws.com:5432/d9l9fi89u8dmua"
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.secret_key = ""
api = Api(app)
db.init_app(app)

jwt = JWT(app, authenticate, identity)  # /auth to check username/password

# @jwt_required for app routes that require auth


@app.before_first_request
def create_tables():
    db.create_all()


@app.route('/')
def hello_world():
    return render_template('index.html')


api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run()
