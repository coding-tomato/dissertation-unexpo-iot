from werkzeug.security import safe_str_cmp
from server.models.user import UserModel

def authenticate(username, password):
    user = UserModel.find_by_user(username)
    print("Checking")
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
    