from urllib.parse import unquote, parse_qs
import json
import hmac
import hashlib
from urllib.parse import unquote

from loader import get_db

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