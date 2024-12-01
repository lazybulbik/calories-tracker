from loader import app, get_db, Database
from flask import request, jsonify, make_response

from MistralLLM import MistralLLM 
from config import GENERATE_PLAN_PROMT

import jwt
import utils
import hmac
import hashlib
import json


@app.route('/api/get_plan')
def get_plan():
    token = request.cookies.get('token')
    db: Database = get_db()

    user_data_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    user_data = db.get_data(filters={'id': user_data_token['user']['id']}, table='users')[0]

    plan = eval(user_data['plan'])

    return jsonify({'status': 'ok', 'message': 'success', 'data': plan}), 200


@app.route('/api/get_user_data')
def get_user_data():
    token = request.cookies.get('token')
    db: Database = get_db()
    date = request.args.get('date')

    user_data_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    user_data = db.get_data(filters={'id': user_data_token['user']['id']}, table='users')[0]
    meals = db.get_data(filters={'owner_id': user_data_token['user']['id'], 'date': date}, table='meals')

    daily_plan = utils.get_curent_user_daily_plan(user_data_token['user']['id'])

    data = {
        'user': user_data,
        'meals': meals,
        'daily_plan': daily_plan
    }

    return jsonify({'status': 'ok', 'message': 'success', 'data': data}), 200