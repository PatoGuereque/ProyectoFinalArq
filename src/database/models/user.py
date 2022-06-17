from sqlalchemy import (
    MetaData,
    Column,
    Integer,
    String,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base(
    metadata=MetaData(),
)


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)

    # plain text for the scope of this project
    # (I do not endorse the use of plain text passwords anywhere)
    user_password = Column(String)

    favorites = Column(String)
    

