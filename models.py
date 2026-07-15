
from sqlalchemy import Column,Integer,String

from database import Base



class User(Base):

    __tablename__="users"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    username = Column(
        String,
        unique=True
    )


    password = Column(
        String
    )


    role = Column(
        String
    )




class Integration(Base):

    __tablename__="integrations"


    id = Column(
        Integer,
        primary_key=True
    )


    name = Column(
        String
    )


    provider = Column(
        String
    )


    api_url = Column(
        String
    )


    status = Column(
        String
    )
