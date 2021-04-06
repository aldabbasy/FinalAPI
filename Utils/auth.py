from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
import hashlib
from Models import User

users = User.User.query.all()

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    print(users)
    user = username_table.get(username, None)
    user_password = user.password.encode('utf-8')
    hashed_posted_password = hashlib.md5(password.encode('utf-8')).hexdigest()
    if user and safe_str_cmp(user_password, hashed_posted_password):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None).id