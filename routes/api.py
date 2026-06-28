from flask import Blueprint
from flask import request
from flask import jsonify

from datetime import datetime

from models import db
from models.tenant import Tenant
from models.metric import Metric

from extensions import socketio

api_bp = Blueprint(
    "api",
    __name__
)


@api_bp.route(
    "/api/v1/ingest",
    methods=["POST"]
)
def ingest():

    data = request.get_json()

    if not data:

        return jsonify({

            "success":False,

            "message":"Invalid JSON"

        }),400

    api_key = data.get("api_key")

    tenant = Tenant.query.filter_by(
        api_key=api_key
    ).first()

    if tenant is None:

        return jsonify({

            "success":False,

            "message":"Invalid API Key"

        }),401

    metric = Metric(

        tenant_id=tenant.id,

        timestamp=datetime.utcnow(),

        revenue=float(
            data.get("revenue",0)
        ),

        visitors=int(
            data.get("visitors",0)
        ),

        orders=int(
            data.get("orders",0)
        ),

        profit=float(
            data.get("profit",0)
        )

    )

    db.session.add(metric)

    db.session.commit()

    socketio.emit(

        "new_metric",

        {

            "tenant":tenant.id,

            "revenue":metric.revenue,

            "visitors":metric.visitors,

            "orders":metric.orders,

            "profit":metric.profit

        }

    )

    return jsonify({

        "success":True,

        "message":"Metric Stored"

    })