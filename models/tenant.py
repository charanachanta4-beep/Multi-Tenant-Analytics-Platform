from datetime import datetime

from flask_login import UserMixin

from models import db

import secrets

class Tenant(UserMixin, db.Model):

    __tablename__ = "tenant"

    id = db.Column(db.Integer, primary_key=True)

    company = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    metrics = db.relationship(
      "Metric",
      backref="tenant",
      cascade="all, delete-orphan",
      lazy=True
    )

    datasources = db.relationship(
      "DataSource",
      backref="tenant",
      cascade="all, delete-orphan",
      lazy=True
    )

    api_key = db.Column(
      db.String(80),
      unique=True,
      nullable=False,
      default=lambda: "bh_live_" + secrets.token_urlsafe(32)
    )

    workspace_name = db.Column(
      db.String(120),
      nullable=True
    )