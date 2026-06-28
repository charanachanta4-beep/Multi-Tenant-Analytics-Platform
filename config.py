import os

class Config:

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "buildhub_super_secret"
    )

    DATABASE_URL = os.getenv("DATABASE_URL")

    if DATABASE_URL:

        # Railway sometimes provides postgres://
        DATABASE_URL = DATABASE_URL.replace(
            "postgres://",
            "postgresql://",
            1
        )

        SQLALCHEMY_DATABASE_URI = DATABASE_URL

    else:

        # Local development
        SQLALCHEMY_DATABASE_URI = "sqlite:///database.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_FOLDER = "uploads"


    MAX_CONTENT_LENGTH = 16 * 1024 * 1024