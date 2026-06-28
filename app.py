from flask import Flask
import os
from config import Config
from models import db

from extensions import (
    bcrypt,
    login_manager,
    socketio
)

from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.upload import upload_bp

from models.tenant import Tenant
from models.metric import Metric
from models.datasource import DataSource

from routes.developer import developer_bp
from routes.notifications import notifications_bp
from routes.profile import profile_bp
from routes.settings import settings_bp
from routes.api import api_bp
from routes.embed import embed_bp
from routes.reports import reports_bp

@login_manager.user_loader
def load_user(user_id):
    return Tenant.query.get(int(user_id))


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    os.makedirs(
      app.config["UPLOAD_FOLDER"],
      exist_ok=True
    )

    # Initialize extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    # Create database tables
    with app.app_context():
        db.create_all()

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(upload_bp)
    app.register_blueprint(notifications_bp)
    app.register_blueprint(developer_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(embed_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(settings_bp)
    socketio.init_app(app)
    return app

app = create_app()
import socket_events


if __name__ == "__main__":
    socketio.run(
        app,
        debug=True
    )