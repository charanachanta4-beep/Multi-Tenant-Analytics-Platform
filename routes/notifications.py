from flask import Blueprint, render_template
from flask_login import login_required, current_user

notifications_bp = Blueprint(
    "notifications",
    __name__
)

@notifications_bp.route("/notifications")
@login_required
def notifications():

    notifications = [

        {
            "icon":"📤",
            "title":"CSV Uploaded",
            "message":"Your CSV file was uploaded successfully.",
            "time":"Today"
        },

        {
            "icon":"📊",
            "title":"Dashboard Updated",
            "message":"Analytics dashboard has been refreshed.",
            "time":"Today"
        },

        {
            "icon":"🔑",
            "title":"API Request",
            "message":"Data received using your API key.",
            "time":"Yesterday"
        },

        {
            "icon":"📄",
            "title":"Report Exported",
            "message":"PDF report generated successfully.",
            "time":"Yesterday"
        }

    ]

    return render_template(
        "notifications.html",
        tenant=current_user,
        notifications=notifications
    )