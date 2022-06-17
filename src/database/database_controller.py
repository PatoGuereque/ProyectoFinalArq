import os
from sqlalchemy import (
    MetaData,
    create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


def get_postgres_uri():
    host = os.environ.get("DB_HOST", "postgres")
    password = os.environ.get("DB_PASS", "abc123")
    user = os.environ.get("DB_USER", "movies")
    db_name = os.environ.get("DB_NAME", "movies")
    port = int(os.environ.get("DB_PORT", "5432"))
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


Base = declarative_base(
    metadata=MetaData(),
)


engine = create_engine(
    get_postgres_uri(),
    isolation_level="REPEATABLE READ",
)

def start_mappers():
    Base.metadata.create_all(engine)

DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        get_postgres_uri(),
        isolation_level="REPEATABLE READ",
    )
)
session = DEFAULT_SESSION_FACTORY()
