from datetime import datetime as dt
from flask import current_app as app, jsonify
from ..Models import User
from .. import db
import json
from ..Utils import AlchemyEncoder

@app.route("/getUsers", methods=["GET"])
def user_records():
    users = User.User.query.all()
    print(users)
    return json.dumps(users, cls=AlchemyEncoder.AlchemyEncoder)

@app.route("/create/<username>/<email>", methods=["POST"])
def create(username,email):

    new_user = User.User(
        username=username,
        email=email,
        createdAt=dt.now(),
    )

    db.session.add(new_user)
    db.session.commit()
    return "created successfuly"
