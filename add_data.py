# !/usr/bin/env python3

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

from database_setup import Base, Data, User

# For localhost
# engine = create_engine('sqlite:///data.db', connect_args={'check_same_thread': False})

# engine = create_engine('mysql+pymysql://b5060ef24e7038:1902c0af@eu-cdbr-west-02.cleardb.net/heroku_ad06423d03e4f02')
# engine = create_engine('postgres://ovwycgfbfuzsee:cb4a0a501c78638240b3e8d421f8db3f4e85762a6aad0411b090f53703e73a98'
# #                        '@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/d1824lvtejfmou')
# engine = create_engine('mysql+pymysql://b5060ef24e7038:1902c0af@eu-cdbr-west-02.cleardb.net/heroku_ad06423d03e4f02')
engine = create_engine('postgres://ovwycgfbfuzsee:cb4a0a501c78638240b3e8d421f8db3f4e85762a6aad0411b090f53703e73a98'
                       '@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/d1824lvtejfmou')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# data
data1 = Data(id=3,
             first_name="Ahmed",
             last_name="Ahmed",
             github_link="https://github.com/yasir-albardawil")

session.add(data1)
session.commit()
