from datetime import datetime as dt
from flask import current_app as app, jsonify, request
from flask_jwt import jwt_required, current_identity
from ..Models import User
from .. import db
import json
from ..Utils import AlchemyEncoder
import hashlib

@app.route("/getUsers", methods=["GET"])
def user_records():
    users = User.User.query.all()
    result = [i.serialize for i in users]
    return jsonify(result)

@app.route("/create", methods=["POST"])
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
