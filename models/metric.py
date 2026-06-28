from models import db


class Metric(db.Model):

    __tablename__ = "metrics"

    id = db.Column(db.Integer, primary_key=True)

    tenant_id = db.Column(
        db.Integer,
        db.ForeignKey("tenant.id"),
        nullable=False
    )

    timestamp = db.Column(
        db.DateTime,
        nullable=False
    )

    revenue = db.Column(
        db.Float,
        default=0
    )

    visitors = db.Column(
        db.Integer,
        default=0
    )

    orders = db.Column(
        db.Integer,
        default=0
    )

    profit = db.Column(
        db.Float,
        default=0
    )