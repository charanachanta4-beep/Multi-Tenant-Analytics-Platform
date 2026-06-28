from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_socketio import SocketIO

bcrypt = Bcrypt()

login_manager = LoginManager()

socketio = SocketIO(
    cors_allowed_origins="*"
)