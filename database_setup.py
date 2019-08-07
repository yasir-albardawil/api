# !/usr/bin/env python3

from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine

Base = declarative_base()


# class to store user information
class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)


# class for Movies Database
class Data(Base):
    __tablename__ = "data"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(250))
    last_name = Column(String(250))
    github_link = Column(String(250))

    @property
    def serialize(self):
        # return data in serializable format
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'github_link': self.github_link,
        }


engine = create_engine('mysql://b5060ef24e7038:1902c0af@eu-cdbr-west-02.cleardb.net/heroku_ad06423d03e4f02')
Base.metadata.create_all(engine)
