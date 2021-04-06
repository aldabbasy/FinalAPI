from flask import current_app as app
from .UserController import bp as usersController

app.register_blueprint(usersController, url_prefix='/api/users')