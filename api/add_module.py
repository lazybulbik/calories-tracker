from loader import app, get_db, Database
from flask import request, jsonify, make_response

from MistralLLM import MistralLLM 
from config import GENERATE_PLAN_PROMT

import jwt
import utils
import hmac
import hashlib
import json


@app.route('/api/search')
def search():
    food_name = request.args.get('food_name')

    serach_results = utils.serach_food(food_name)

    return jsonify({'status': 'ok', 'message': 'success', 'data': serach_results}), 200


@app.route('/api/add_food', methods=['POST'])
def add_food():
    token = request.cookies.get('token')
    db: Database = get_db()

    user_data_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    user_data = db.get_data(filters={'id': user_data_token['user']['id']}, table='users')[0]

    data = request.get_json()
    food_id = utils.generate_random_key(20)
    date = data['date']
    meal = data['meal']
    weight = data['weight']

    utils.add_food(user_data_token['user']['id'], food_id, meal, weight)

    return jsonify({'status': 'ok', 'message': 'success'}), 200