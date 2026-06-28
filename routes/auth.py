from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import current_user

from extensions import bcrypt

from models import db

from models.tenant import Tenant

auth_bp = Blueprint(
    "auth",
    __name__
)


@auth_bp.route("/")
def home():

    if current_user.is_authenticated:
        return redirect(url_for("dashboard.dashboard"))

    return redirect(url_for("auth.login"))


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]

        password = request.form["password"]

        tenant = Tenant.query.filter_by(
            email=email
        ).first()

        if tenant:

            if bcrypt.check_password_hash(
                tenant.password,
                password
            ):

                login_user(tenant)

                return redirect(
                    url_for("dashboard.dashboard")
                )

        flash("Invalid Credentials")

    return render_template("login.html")


@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        company = request.form["company"]

        email = request.form["email"]

        password = request.form["password"]

        existing = Tenant.query.filter_by(
            email=email
        ).first()

        if existing:

            flash("Email already exists")

            return redirect(
                url_for("auth.register")
            )

        hashed = bcrypt.generate_password_hash(
            password
        ).decode("utf-8")

        tenant = Tenant(
            company=company,
            email=email,
            password=hashed
        )

        db.session.add(tenant)

        db.session.commit()

        flash("Account Created Successfully")

        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth_bp.route("/logout")
@login_required
def logout():

    logout_user()

    return redirect(
        url_for("auth.login")
    )