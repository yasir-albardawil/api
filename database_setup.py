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


# For localhost
# engine = create_engine('sqlite:///data.db', connect_args={'check_same_thread': False})

# engine = create_engine('mysql+pymysql://b5060ef24e7038:1902c0af@eu-cdbr-west-02.cleardb.net/heroku_ad06423d03e4f02')
# engine = create_engine('postgres://ovwycgfbfuzsee:cb4a0a501c78638240b3e8d421f8db3f4e85762a6aad0411b090f53703e73a98'
# #                        '@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/d1824lvtejfmou')
# engine = create_engine('postgres://ovwycgfbfuzsee:cb4a0a501c78638240b3e8d421f8db3f4e85762a6aad0411b090f53703e73a98'
#                        '@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/d1824lvtejfmou')
engine = create_engine('mysql+pymysql://b5060ef24e7038:1902c0af@eu-cdbr-west-02.cleardb.net/heroku_ad06423d03e4f02')
Base.metadata.create_all(engine)
