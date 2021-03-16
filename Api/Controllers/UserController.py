from datetime import datetime as dt
from flask import current_app as app, jsonify, request
from ..Models import User
from .. import db
import json
from ..Utils import AlchemyEncoder

@app.route("/getUsers", methods=["GET"])
def user_records():
    users = User.User.query.all()
    result = [i.serialize for i in users]
    return jsonify(result)

@app.route("/create", methods=["POST"])
def create():
    request_body = request.json
    new_user = User.User(
        username=request_body["username"],
        email=request_body["email"],
        createdAt=dt.now(),
    )

    db.session.add(new_user)
    db.session.commit()
    return "created successfuly"
