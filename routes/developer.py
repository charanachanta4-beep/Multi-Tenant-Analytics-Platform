import secrets

from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from models import db

developer_bp = Blueprint("developer", __name__)


@developer_bp.route("/developer")
@login_required
def developer():
    return render_template(
        "developer.html",
        tenant=current_user
    )


@developer_bp.route("/developer/regenerate", methods=["POST"])
@login_required
def regenerate():

    current_user.api_key = "bh_live_" + secrets.token_urlsafe(32)

    db.session.commit()

    return redirect(url_for("developer.developer"))