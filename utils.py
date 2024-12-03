from urllib.parse import unquote, parse_qs
import json
import hmac
import hashlib
from urllib.parse import unquote

import time
import requests

from loader import get_db, Database


def validate(hash_str, init_data, token, c_str="WebAppData"):
    init_data = sorted([ chunk.split("=") 
          for chunk in unquote(init_data).split("&") 
            if chunk[:len("hash=")]!="hash="],
        key=lambda x: x[0])
    init_data = "\n".join([f"{rec[0]}={rec[1]}" for rec in init_data])

    secret_key = hmac.new(c_str.encode(), token.encode(),
        hashlib.sha256 ).digest()
    data_check = hmac.new( secret_key, init_data.encode(),
        hashlib.sha256)

    return data_check.hexdigest() == hash_str


def parse_telegram_web_app_data(data_string):
    # Убираем начальный символ # если есть
    if data_string.startswith('#'):
        data_string = data_string[1:]
    
    # Разбиваем строку на параметры
    params = parse_qs(data_string)
    
    result = {}
    
    # Обрабатываем каждый параметр
    for key, value in params.items():
        # Берем первое значение, так как parse_qs всегда возвращает список
        value = value[0]
        
        # Особая обработка для tgWebAppData
        if key == 'tgWebAppData':
            # Разбираем внутренние параметры
            inner_params = parse_qs(value)
            web_app_data = {}
            
            for inner_key, inner_value in inner_params.items():
                inner_value = inner_value[0]
                if inner_key == 'user':
                    # Декодируем user дважды и преобразуем в JSON
                    try:
                        user_data = unquote(unquote(inner_value))
                        web_app_data['user'] = json.loads(user_data)
                    except:
                        web_app_data['user'] = inner_value
                else:
                    web_app_data[inner_key] = inner_value
            
            result[key] = web_app_data
        
        # Обработка tgWebAppThemeParams
        elif key == 'tgWebAppThemeParams':
            try:
                result[key] = json.loads(unquote(value))
            except:
                result[key] = value
        
        # Все остальные параметры
        else:
            result[key] = value
    
    return result


def is_registered(user_id):
    return bool(get_db().get_data(filters={'id': user_id}, table='users'))


def new_user(id, sex, height, weight, birthday, goal, experience):
    new_data = {
        'id': id,
        'sex': sex,
        'height': height,
        'weight': weight,
        'birthday': birthday,
        'goal': goal,
        'experience': experience,
        'premium': 0,
        'timestamp': int(time.time())
    }

    db: Database = get_db()

    if is_registered(id):
        db.update_data(data=new_data, table='users', filters={'id': id})
        return
    
    db.new_write(new_data, 'users')


def get_curent_user_daily_plan(user_id):
    db = get_db()

    user_data = db.get_data(filters={'id': user_id}, table='users')[0]
    print(user_data['plan'])
    user_plan = eval(user_data['plan'])
    user_plan.reverse()

    for week in user_plan:
        if week['is_reached']:
            return week


def serach_food(food_name):
    url = f'http://dietagram.com/_next/data/XZZs7l3pvagiUKt5TXFX7/Russian/calories/{food_name}.json'

    response = requests.get(url)
    data = response.json()

    return data['pageProps']['dishes']['dishes']


def generate_random_key(length):
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=length))


def add_food(user_id, meal_time, product, date):
    db: Database = get_db()

    user_meals = db.get_data(filters={'owner_id': user_id, 'date': date}, table='meals')

    if not user_meals:
        products_data = {
            'breakfast': [],
            'lunch': [],
            'dinner': [],
            'snack': [],
            'total_calories': 0,
            'total_carbs': 0,
            'total_proteins': 0,
            'total_fats': 0
        }

        products_data[meal_time].append(product)
        products_data['total_calories'] += product['calories']
        products_data['total_carbs'] += product['carbs']
        products_data['total_proteins'] += product['proteins']
        products_data['total_fats'] += product['fats']

        new_data = {
            'products': str(products_data),
            'owner_id': user_id,
            'date': date
        }

        db.new_write(new_data, 'meals')        

    else:
        products_data = eval(user_meals[0]['products'])
        products_data[meal_time].append(product)
        products_data['total_calories'] += product['calories']
        products_data['total_carbs'] += product['carbs']
        products_data['total_proteins'] += product['proteins']
        products_data['total_fats'] += product['fats']

        new_data = {
            'products': str(products_data),
            'owner_id': user_id,
            'date': date
        }

        db.update_data(data=new_data, table='meals', filters={'owner_id': user_id, 'date': date})
