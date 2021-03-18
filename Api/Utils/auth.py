from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from ..Models import User

users = User.User.query.all()

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    print(users)
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)