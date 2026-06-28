from flask import Blueprint, render_template, abort
from sqlalchemy import func

from models.metric import Metric
from models.tenant import Tenant

embed_bp = Blueprint(
    "embed",
    __name__
)


@embed_bp.route("/embed/<api_key>")
def embed_dashboard(api_key):

    tenant = Tenant.query.filter_by(
        api_key=api_key
    ).first()

    if tenant is None:
        abort(404)

    revenue = (
        Metric.query.with_entities(
            func.sum(Metric.revenue)
        )
        .filter_by(tenant_id=tenant.id)
        .scalar()
        or 0
    )

    visitors = (
        Metric.query.with_entities(
            func.sum(Metric.visitors)
        )
        .filter_by(tenant_id=tenant.id)
        .scalar()
        or 0
    )

    orders = (
        Metric.query.with_entities(
            func.sum(Metric.orders)
        )
        .filter_by(tenant_id=tenant.id)
        .scalar()
        or 0
    )

    profit = (
        Metric.query.with_entities(
            func.sum(Metric.profit)
        )
        .filter_by(tenant_id=tenant.id)
        .scalar()
        or 0
    )

    metrics = (
        Metric.query
        .filter_by(tenant_id=tenant.id)
        .order_by(Metric.timestamp.asc())
        .all()
    )

    labels = [
        m.timestamp.strftime("%d %b")
        for m in metrics
    ]

    revenue_values = [
        m.revenue
        for m in metrics
    ]

    visitors_values = [
        m.visitors
        for m in metrics
    ]

    orders_values = [
        m.orders
        for m in metrics
    ]

    return render_template(

        "embed.html",

        tenant=tenant,

        revenue=revenue,

        visitors=visitors,

        orders=orders,

        profit=profit,

        labels=labels,

        revenue_values=revenue_values,

        visitors_values=visitors_values,

        orders_values=orders_values

    )