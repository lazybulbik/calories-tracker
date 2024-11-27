from loader import app, get_db, Database
from flask import request, jsonify, make_response

from MistralLLM import MistralLLM 
from config import GENERATE_PLAN_PROMT

import jwt
import utils
import hmac
import hashlib
import json


@app.route('/api/register', methods=['POST'])
def register_api():
    data = request.get_json()

    token = request.cookies.get('token')
    user_data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])

    sex = data['sex']
    height = data['height']
    weight = data['weight']
    birthday = data['birthday']
    goal = data['goal']
    experience = data['experience']

    user_id = user_data['user']['id']

    utils.new_user(user_id, sex, height, weight, birthday, goal, experience)

    return jsonify({'status': 'ok', 'message': 'success'}), 200


@app.route('/api/make_plan', methods=['POST'])
def make_plan():
    token = request.cookies.get('token')
    db: Database = get_db()

    user_data_token = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
    user_data = db.get_data(filters={'id': user_data_token['user']['id']}, table='users')[0]

    individual_parameters = (f'Год рождения: {user_data["birthday"]}\n' 
                            f'Пол: {user_data["sex"]}\n'
                            f'Рост: {user_data["height"]}\n'
                            f'Вес: {user_data["weight"]}\n'
                            f'Цель: {user_data["goal"]}\n'
                            f'Опыт: {user_data["experience"]}\n')

    answer = MistralLLM().generate(GENERATE_PLAN_PROMT + f'\n{individual_parameters}')

    try:
        answer = answer.replace('\\n', '').replace('```', '').replace('json', '')
        print('\n')
        answer = answer.replace("'", '"')        

        if not answer.startswith('['):
            answer = '[' + answer
        if not answer.endswith(']'):
            answer = answer + ']'

        print(answer)
        answer = json.loads(answer)
    except Exception as e:
        print(e)
        return jsonify({'status': 'error', 'message': 'invalid answer'}), 400

    db.update_data(data={'plan': str(answer)}, filters={'id': user_data_token['user']['id']}, table='users')


    return jsonify({'status': 'ok', 'message': 'success', 'data': answer}), 200