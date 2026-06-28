from flask import Blueprint, render_template
from flask_login import login_required, current_user
from sqlalchemy import func

from models import db
from models.metric import Metric
from models.datasource import DataSource

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


@dashboard_bp.route("/dashboard")
@login_required
def dashboard():

    # -------------------------
    # KPI Totals
    # -------------------------

    revenue = db.session.query(
        func.sum(Metric.revenue)
    ).filter(
        Metric.tenant_id == current_user.id
    ).scalar() or 0

    visitors = db.session.query(
        func.sum(Metric.visitors)
    ).filter(
        Metric.tenant_id == current_user.id
    ).scalar() or 0

    orders = db.session.query(
        func.sum(Metric.orders)
    ).filter(
        Metric.tenant_id == current_user.id
    ).scalar() or 0

    profit = db.session.query(
        func.sum(Metric.profit)
    ).filter(
        Metric.tenant_id == current_user.id
    ).scalar() or 0

    # -------------------------
    # Revenue Chart
    # -------------------------

    chart_rows = Metric.query.filter_by(
        tenant_id=current_user.id
    ).order_by(
        Metric.timestamp.asc()
    ).all()

    labels = [
        row.timestamp.strftime("%d %b")
        for row in chart_rows
    ]

    revenue_values = [
        row.revenue
        for row in chart_rows
    ]

    visitors_values = [
        row.visitors
        for row in chart_rows
    ]

    orders_values = [
        row.orders
        for row in chart_rows
    ]

    profit_values = [
        row.profit
        for row in chart_rows
    ]

    # -------------------------
    # Recent Metrics
    # -------------------------

    metrics = Metric.query.filter_by(
        tenant_id=current_user.id
    ).order_by(
        Metric.timestamp.desc()
    ).limit(20).all()

    # -------------------------
    # Recent Uploads
    # -------------------------

    uploads = DataSource.query.filter_by(
        tenant_id=current_user.id
    ).order_by(
        DataSource.uploaded_at.desc()
    ).all()

    return render_template(

        "dashboard.html",

        tenant=current_user,

        revenue=revenue,

        visitors=visitors,

        orders=orders,

        profit=profit,

        labels=labels,

        revenue_values=revenue_values,

        visitors_values=visitors_values,

        orders_values=orders_values,

        profit_values=profit_values,

        metrics=metrics,

        uploads=uploads

    )