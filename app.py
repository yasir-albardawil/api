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
engine = create_engine('sqlite:///data.db', connect_args={'check_same_thread': False})
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


@app.route('/')
def show_data():
    return render_template('index.html')


@app.route('/data.json')
@token_required
def data():
    data = session.query(Data).all()
    return jsonify(data=[d.serialize for d in data])


@app.route('/login')
def login():
    auth = request.authorization
    # 'exp': datetime.datetime.now() + datetime.timedelta(days=100000)
    # jsonify({'token': token.decode('UTF-8')})
    if auth and auth.username == 'yasir' and auth.password == 'password':
        token = jwt.encode({'user': auth.username},
                           app.config['SECRET_KEY'])
        return render_template('login.html', token=token.decode('UTF-8'))
    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required'})


if __name__ == '__main__':
    app.run(threads=False)
