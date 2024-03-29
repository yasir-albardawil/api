#!/usr/bin/env python3
import secrets
from functools import wraps
import jwt
from flask import Flask, jsonify, request, make_response, render_template
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Data

app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(256)
# Connect to Database and create database session

# For localhost
# engine = create_engine('sqlite:///data.db', connect_args={'check_same_thread': False})

# engine = create_engine('mysql+pymysql://b5060ef24e7038:1902c0af@eu-cdbr-west-02.cleardb.net/heroku_ad06423d03e4f02')
engine = create_engine('postgres://ovwycgfbfuzsee:cb4a0a501c78638240b3e8d421f8db3f4e85762a6aad0411b090f53703e73a98'
                       '@ec2-54-228-246-214.eu-west-1.compute.amazonaws.com:5432/d1824lvtejfmou')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'Token is missing'}), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'message': 'Token is invalid'}), 403

        return f(*args, **kwargs)

    return decorated


@app.route('/data.json')
@token_required
def data():
    data = session.query(Data).all()
    return jsonify(data=[d.serialize for d in data])


@app.route('/')
def view_data():
    auth = request.authorization
    # 'exp': datetime.datetime.now() + datetime.timedelta(days=100000)
    # jsonify({'token': token.decode('UTF-8')})
    if auth and auth.username == 'yasir' and auth.password == 'password':
        token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)},
                           app.config['SECRET_KEY'])
        return render_template('index.html', token=token.decode('UTF-8'))
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required'})


if __name__ == '__main__':
    app.run(threads=False)
