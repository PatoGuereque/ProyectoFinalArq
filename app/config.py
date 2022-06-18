import os

class Config:
    USER = os.environ.get("DB_USER", "movies")
    PASSWORD = os.environ.get("DB_PASS", "abc123")
    HOST = os.environ.get("DB_HOST", "postgres")
    DB_NAME = os.environ.get("DB_NAME", "movies")
    PORT = int(os.environ.get("DB_PORT", "5432"))
    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}"
    DEBUG = False