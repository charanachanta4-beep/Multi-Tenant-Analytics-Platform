from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import current_app

from flask_login import login_required
from flask_login import current_user

from werkzeug.utils import secure_filename

from models import db
from models.metric import Metric
from models.datasource import DataSource

from services.csv_parser import validate_csv

from dateutil.parser import parse

import os

upload_bp = Blueprint(
    "upload",
    __name__
)


@upload_bp.route("/upload", methods=["GET", "POST"])
@login_required
def upload():

    if request.method == "GET":
        return render_template("upload.html")

    # -----------------------------
    # Check uploaded file
    # -----------------------------

    if "csvfile" not in request.files:

        flash("Please choose a CSV file.", "danger")

        return redirect(url_for("upload.upload"))

    file = request.files["csvfile"]

    if file.filename == "":

        flash("No file selected.", "danger")

        return redirect(url_for("upload.upload"))

    # -----------------------------
    # Save file
    # -----------------------------

    filename = secure_filename(file.filename)

    upload_folder = current_app.config["UPLOAD_FOLDER"]

    os.makedirs(upload_folder, exist_ok=True)

    filepath = os.path.join(upload_folder, filename)

    file.save(filepath)

    # -----------------------------
    # Validate CSV
    # -----------------------------

    valid, result = validate_csv(filepath)

    if not valid:

        flash(result, "danger")

        return redirect(url_for("upload.upload"))

    df = result["dataframe"]

    timestamp_column = result["timestamp"]

    # -----------------------------
    # Save datasource
    # -----------------------------

    datasource = DataSource(

        tenant_id=current_user.id,

        source_type="CSV",

        filename=filename

    )

    db.session.add(datasource)

    inserted = 0

    # -----------------------------
    # Store every row
    # -----------------------------

    for _, row in df.iterrows():

        try:

            timestamp = parse(str(row[timestamp_column]))

        except:

            continue

        metric = Metric(

            tenant_id=current_user.id,

            timestamp=timestamp,

            revenue=float(row.get("revenue", 0) or 0),

            visitors=int(float(row.get("visitors", 0) or 0)),

            orders=int(float(row.get("orders", 0) or 0)),

            profit=float(row.get("profit", 0) or 0)

        )

        db.session.add(metric)

        inserted += 1

    db.session.commit()

    flash(
        f"{inserted} rows imported successfully!",
        "success"
    )

    return redirect(
        url_for("dashboard.dashboard")
    )