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
def add_food_api():
    token = request.cookies.get('token')
    db: Database = get_db()

    user_data_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    user_data = db.get_data(filters={'id': user_data_token['user']['id']}, table='users')[0]

    data = request.get_json()
    food_id = utils.generate_random_key(20)
    date = data['date']
    product = data['product']
    meal_time = data['meal_time']

    utils.add_food(user_data_token['user']['id'], meal_time=meal_time, product=product, date=date)

    return jsonify({'status': 'ok', 'message': 'success'}), 200


@app.route('/api/delete_food', methods=['POST'])
def delete_food_api():
    token = request.cookies.get('token')
    db: Database = get_db()

    user_data_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    user_data = db.get_data(filters={'id': user_data_token['user']['id']}, table='users')[0]

    data = request.get_json()
    food_id = data['food_id']
    date = data['date']
    meal_time = data['meal_time']

    utils.delete_food(user_data_token['user']['id'], food_id=food_id, date=date, meal_time=meal_time)

    meals = db.get_data(filters={'owner_id': user_data_token['user']['id'], 'date': date}, table='meals')
    products = eval(meals[0]['products'])

    return jsonify({'status': 'ok', 'message': 'success', 'data': products[meal_time]}), 200



@app.route('/api/get_recent_food')
def get_recent_food_api():
    token = request.cookies.get('token')
    db: Database = get_db()

    user_data_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    user_data = db.get_data(filters={'id': user_data_token['user']['id']}, table='users')[0]

    recent_food = utils.get_recent_food(user_data_token['user']['id'])

    return jsonify({'status': 'ok', 'message': 'success', 'data': recent_food}), 200