import json
import hashlib
from flask import Blueprint, current_app as app
from datetime import datetime as dt
from flask import jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from Models.User import User
from wsgi import db

bp = Blueprint('users', __name__)

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    user = User.query.filter_by(username=username).first()
    if authenticate(username, password):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token)
    
    return jsonify({"msg": "Bad username or password"}), 401

@bp.route("/getUsers", methods=["GET"])
def user_records():
    users = User.query.all()
    result = [i.serialize for i in users]
    return jsonify(result)

@bp.route("/create", methods=["POST"])
@jwt_required()
def create():
    request_body = request.json
    hashed_password = hashlib.md5(request_body["password"].encode('utf-8')).hexdigest()
    new_user = User(
        username= request_body["username"],
        email= request_body["email"],
        password= hashed_password,
        createdBy= get_jwt_identity(),
        createdAt= dt.now(),
    )
    db.session.add(new_user)
    db.session.commit()
    return "created successfuly"
