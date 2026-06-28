from datetime import datetime

from models import db


class DataSource(db.Model):

    __tablename__ = "datasource"

    id = db.Column(db.Integer, primary_key=True)

    tenant_id = db.Column(
        db.Integer,
        db.ForeignKey("tenant.id"),
        nullable=False
    )

    source_type = db.Column(db.String(50))

    filename = db.Column(db.String(200))

    uploaded_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )