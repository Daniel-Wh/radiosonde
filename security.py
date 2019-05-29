from models.user_model import UserModel
from werkzeug.security import safe_str_cmp


# authenticates user for security
def authenticate(username, password):
    user = UserModel.find_by_username(username)  # returns user with specified username
    # if user and password are true then return the user
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id) # returns user based on their id, or None if not found
