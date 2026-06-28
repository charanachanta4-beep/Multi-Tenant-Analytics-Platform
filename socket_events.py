from flask_login import current_user
from flask_socketio import join_room

from extensions import socketio


@socketio.on("connect")
def handle_connect():

    if current_user.is_authenticated:

        join_room(f"tenant_{current_user.id}")

        print(f"Tenant {current_user.id} Connected")