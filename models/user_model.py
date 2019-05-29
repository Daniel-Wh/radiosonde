from db import db


# class that models a user
class UserModel(db.Model):

    __tablename__ = "users"  # table name is users

    id = db.Column(db.INTEGER, primary_key=True)  # column in table for id for user, auto incremented
    username = db.Column(db.String(40))  # column in table for the user's username that is entered at login, no repeats
    password = db.Column(db.String(40))  # column in table for the user's password that is entered at login, no repeats

    # initializes instance of UserModel with the data for all columns given as parameters
    def __init__(self, username, password):
        self.username = username
        self.password = password

    # saves the UserModel to the database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # finds a row by specific username given as a parameter
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    # finds a row by specific id given as a parameter
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
