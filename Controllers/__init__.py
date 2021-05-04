from flask import current_app as app
from .UserController import bp as usersController
from .AuthController import bp as authController

app.register_blueprint(authController, url_prefix='/api/auth')
app.register_blueprint(usersController, url_prefix='/api/users')
