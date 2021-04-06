import json
import hashlib
from flask import Blueprint
from datetime import datetime as dt
from flask import jsonify, request
from flask_jwt import jwt_required, current_identity
from Models import User
from wsgi import db

bp = Blueprint('users', __name__)

@bp.route("/getUsers", methods=["GET"])
def user_records():
    users = User.User.query.all()
    result = [i.serialize for i in users]
    return jsonify(result)

@bp.route("/create", methods=["POST"])
@jwt_required()
def create():
    request_body = request.json
    hashed_password = hashlib.md5(request_body["password"].encode('utf-8')).hexdigest()
    new_user = User.User(
        username= request_body["username"],
        email= request_body["email"],
        password= hashed_password,
        createdBy= '%s' % current_identity,
        createdAt= dt.now(),
    )
    db.session.add(new_user)
    db.session.commit()
    return "created successfuly"
