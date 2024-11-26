from loader import app, get_db
from flask import request, jsonify, make_response

import jwt
import utils
import hmac
import hashlib

import json


@app.route('/api/auth', methods=['POST'])
def auth():
    data = request.get_json()

    check_data = data['data_check_string']

    cookies = request.cookies
    if 'tgWebAppData' not in check_data:
        if cookies.get('token'):
            return {
                'status': 'ok',
                'message': 'success'
            }
        return {
            'status': 'error',
            'message': 'tgWebAppData not found'
        }
        
    init_data = data['data_check_string']['tgWebAppData']
    pretty_data = utils.parse_telegram_web_app_data(check_data['tgWebAppData'])
    pretty_data['user'] = json.loads(pretty_data['user'])
    hash = pretty_data['hash']

    if utils.validate(hash, init_data, app.config['SECRET_KEY']):
        token = jwt.encode({
            'user': pretty_data['user']
        }, app.config['SECRET_KEY'])

        print(pretty_data)

        if utils.is_registered(pretty_data['user']['id']):
            response = make_response(jsonify({
                'status': 'ok',
                'message': 'success'
            }))
        else:
            response = make_response(jsonify({
                'status': 'need_register',
                'message': 'user not registered'
            }))
            
        response.set_cookie('token', token, httponly=True, samesite='None', secure=True)
        return response

    else:
        return {
            'status': 'error',
            'message': 'invalid data'
        }