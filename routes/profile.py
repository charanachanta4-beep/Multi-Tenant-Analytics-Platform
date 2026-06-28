from flask import Blueprint, render_template
from flask_login import login_required, current_user

from models.metric import Metric
from models.datasource import DataSource

profile_bp = Blueprint(
    "profile",
    __name__
)


@profile_bp.route("/profile")
@login_required
def profile():

    uploads = DataSource.query.filter_by(
        tenant_id=current_user.id
    ).count()

    metrics = Metric.query.filter_by(
        tenant_id=current_user.id
    ).count()

    return render_template(

        "profile.html",

        tenant=current_user,

        uploads=uploads,

        metrics=metrics

    )