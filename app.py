from flask import Flask, render_template
from flask_restful import Api, reqparse
from flask_jwt import JWT, jwt_required
from security import authenticate, identity
from resources.user_resource import UserRegister
from resources.vis_resource import Visual
from models.station_model import StationData, StationModel
from db import db

uri = "postgres://keujsruvqpelne:291827d8388be8155c772e76b509b9f4ef0e9e81b2aef479644628d60aa11c9b@ec2-" \
      "54-83-205-27.compute-1.amazonaws.com:5432/d9l9fi89u8dmua"
app = Flask(__name__)  # creates flask app
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = uri  # sets database location
app.secret_key = ""
api = Api(app)
db.init_app(app)

jwt = JWT(app, authenticate, identity)  # /auth to check username/password

# @jwt_required for app routes that require auth


# creates the tables for the database before any requests can be made to the api
@app.before_first_request
def create_tables():
    db.create_all()


# creates homepage that returns the html file
@app.route('/')
def home():
    return render_template('index.html')


@app.route('/vis')
def vis():
    return render_template(Visual.render_to())


api.add_resource(UserRegister, '/register')
api.add_resource(Visual, '/vis')

# if the app is called, run the app with debug=True
if __name__ == '__main__':
    app.run(debug=True)
