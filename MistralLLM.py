import config
import requests


class MistralLLM:
    def create_chat(self, promt, file_url=None, filename=None):
        cookies = {
            'cc_cookie': '%7B%22categories%22%3A%5B%22necessary%22%5D%2C%22revision%22%3A1%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-11-20T19%3A02%3A36.823Z%22%2C%22consentId%22%3A%2212fd04af-4af6-48a3-8531-b7cf317849d1%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22support%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-11-20T19%3A02%3A36.823Z%22%2C%22expirationTime%22%3A1747854156824%7D',
            'csrf_token_1d61ec8f0158ec4868343239ec73dbe1bfebad9908ad860e62f470c767573d0d': '6gY50KZbnl2NSUD59+ko1I5hAky72+HN12ht0XeTc1s=',
            'ory_session_coolcurranf83m3srkfl': 'MTczMjEyOTM0NXx6V1ZmR1NBRW8zYmdBOXQ0dExwS2hZMnhaWW4zRmpHRzdndlo1RUJ2bnY4c1ZOT01ubHNramJKRVlTLUU5NTN3RXpULXpkQWs0STBBQWVBSnJiS0x5blZlSFEwbldRQXBSRjBseVYwWjVSTWhzaHQzdjNmbXhGWlp2LVRFSTQwa0NraEdUZGNocjFXdno0aGRsODRVdWpIbjRMcGFaTVByU0QtdW92b0E2NXhPa3JmeDZIMG9QXzh6Y1ZNMHNyMlYwVjFKVWZwWjVZR3lGWXI2MkJVWVc2TVRyVlNod1BBZno1N2ZIYTFfUG5HX1huSmZISjBkdThuQUxNdzVvRG1kTC1ZczlIUkQ1LTNnVXhzSjB3Vml88Zdm3aoVHYI1BWZT_zv2pC2AAxlr0pfGNFpIopPgrbE=',
            'ory_kratos_continuity': 'MTczMjEyOTM0MnxEWDhFQVFMX2dBQUJFQUVRQUFCZl80QUFBUVp6ZEhKcGJtY01Jd0FoYjNKNVgydHlZWFJ2YzE5dmFXUmpYMkYxZEdoZlkyOWtaVjl6WlhOemFXOXVCbk4wY21sdVp3d21BQ1F4T1RVM1pqWTRPQzAzWXpnMkxUUTNPVGN0WW1JMU1pMWxZbVJpWW1OaE16QmtZakU9fPLGXdybf2DxKxccQVR7jNKzSWXgVW-ilTeOUWw6goRU',
            '_cfuvid': 'UeuH605FiAbN7_HEToLsQyQw.T.LhOrDyzuTEHJT6hM-1732129336257-0.0.1.1-604800000',
            'NEXT_LOCALE': 'en',
        }

        headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Accept-Language': 'ru',
            'Sec-Fetch-Mode': 'cors',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://chat.mistral.ai',
            # 'Content-Length': '77',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6.1 Safari/605.1.15',
            'Referer': 'https://chat.mistral.ai/chat',
            'Connection': 'keep-alive',
            'Host': 'chat.mistral.ai',
            'Sec-Fetch-Dest': 'empty',
            # 'Cookie': 'cc_cookie=%7B%22categories%22%3A%5B%22necessary%22%5D%2C%22revision%22%3A1%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-11-20T19%3A02%3A36.823Z%22%2C%22consentId%22%3A%2212fd04af-4af6-48a3-8531-b7cf317849d1%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22support%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-11-20T19%3A02%3A36.823Z%22%2C%22expirationTime%22%3A1747854156824%7D; csrf_token_1d61ec8f0158ec4868343239ec73dbe1bfebad9908ad860e62f470c767573d0d=6gY50KZbnl2NSUD59+ko1I5hAky72+HN12ht0XeTc1s=; ory_session_coolcurranf83m3srkfl=MTczMjEyOTM0NXx6V1ZmR1NBRW8zYmdBOXQ0dExwS2hZMnhaWW4zRmpHRzdndlo1RUJ2bnY4c1ZOT01ubHNramJKRVlTLUU5NTN3RXpULXpkQWs0STBBQWVBSnJiS0x5blZlSFEwbldRQXBSRjBseVYwWjVSTWhzaHQzdjNmbXhGWlp2LVRFSTQwa0NraEdUZGNocjFXdno0aGRsODRVdWpIbjRMcGFaTVByU0QtdW92b0E2NXhPa3JmeDZIMG9QXzh6Y1ZNMHNyMlYwVjFKVWZwWjVZR3lGWXI2MkJVWVc2TVRyVlNod1BBZno1N2ZIYTFfUG5HX1huSmZISjBkdThuQUxNdzVvRG1kTC1ZczlIUkQ1LTNnVXhzSjB3Vml88Zdm3aoVHYI1BWZT_zv2pC2AAxlr0pfGNFpIopPgrbE=; ory_kratos_continuity=MTczMjEyOTM0MnxEWDhFQVFMX2dBQUJFQUVRQUFCZl80QUFBUVp6ZEhKcGJtY01Jd0FoYjNKNVgydHlZWFJ2YzE5dmFXUmpYMkYxZEdoZlkyOWtaVjl6WlhOemFXOXVCbk4wY21sdVp3d21BQ1F4T1RVM1pqWTRPQzAzWXpnMkxUUTNPVGN0WW1JMU1pMWxZbVJpWW1OaE16QmtZakU9fPLGXdybf2DxKxccQVR7jNKzSWXgVW-ilTeOUWw6goRU; _cfuvid=UeuH605FiAbN7_HEToLsQyQw.T.LhOrDyzuTEHJT6hM-1732129336257-0.0.1.1-604800000; NEXT_LOCALE=en',
            'baggage': 'sentry-environment=production,sentry-release=e06f8a7f90d74b679780e538786f31256c8495f0,sentry-public_key=f45309fe00350c22253424f36dd157d8,sentry-trace_id=53505639706a47f0b9f05c092c3411b4,sentry-sample_rate=0.01,sentry-sampled=false',
            'sentry-trace': '53505639706a47f0b9f05c092c3411b4-895b6111387be7c3-0',
        }

        params = {
            'batch': '1',
        }

        json_data = {
            '0': {
                'json': {
                    'content': promt,
                    'files': [],
                    'model': 'pandragon',
                    'features': [],
                },
            },
        }

        if file_url and filename:
            json_data['0']['json']['files'] = [
                {
                    'name': filename,
                    'url': file_url,
                    'type': 'image',
                },
            ]

        response = requests.post(
            'https://chat.mistral.ai/api/trpc/message.newChat',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
        )

        return response.json()[0]['result']['data']['json']['chatId']

    def start_new_chat(self, chat_id):
        cookies = {
            'cc_cookie': '%7B%22categories%22%3A%5B%22necessary%22%5D%2C%22revision%22%3A1%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-11-20T19%3A02%3A36.823Z%22%2C%22consentId%22%3A%2212fd04af-4af6-48a3-8531-b7cf317849d1%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22support%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-11-20T19%3A02%3A36.823Z%22%2C%22expirationTime%22%3A1747854156824%7D',
            'csrf_token_1d61ec8f0158ec4868343239ec73dbe1bfebad9908ad860e62f470c767573d0d': '6gY50KZbnl2NSUD59+ko1I5hAky72+HN12ht0XeTc1s=',
            'ory_session_coolcurranf83m3srkfl': 'MTczMjEyOTM0NXx6V1ZmR1NBRW8zYmdBOXQ0dExwS2hZMnhaWW4zRmpHRzdndlo1RUJ2bnY4c1ZOT01ubHNramJKRVlTLUU5NTN3RXpULXpkQWs0STBBQWVBSnJiS0x5blZlSFEwbldRQXBSRjBseVYwWjVSTWhzaHQzdjNmbXhGWlp2LVRFSTQwa0NraEdUZGNocjFXdno0aGRsODRVdWpIbjRMcGFaTVByU0QtdW92b0E2NXhPa3JmeDZIMG9QXzh6Y1ZNMHNyMlYwVjFKVWZwWjVZR3lGWXI2MkJVWVc2TVRyVlNod1BBZno1N2ZIYTFfUG5HX1huSmZISjBkdThuQUxNdzVvRG1kTC1ZczlIUkQ1LTNnVXhzSjB3Vml88Zdm3aoVHYI1BWZT_zv2pC2AAxlr0pfGNFpIopPgrbE=',
            'ory_kratos_continuity': 'MTczMjEyOTM0MnxEWDhFQVFMX2dBQUJFQUVRQUFCZl80QUFBUVp6ZEhKcGJtY01Jd0FoYjNKNVgydHlZWFJ2YzE5dmFXUmpYMkYxZEdoZlkyOWtaVjl6WlhOemFXOXVCbk4wY21sdVp3d21BQ1F4T1RVM1pqWTRPQzAzWXpnMkxUUTNPVGN0WW1JMU1pMWxZbVJpWW1OaE16QmtZakU9fPLGXdybf2DxKxccQVR7jNKzSWXgVW-ilTeOUWw6goRU',
            '_cfuvid': 'UeuH605FiAbN7_HEToLsQyQw.T.LhOrDyzuTEHJT6hM-1732129336257-0.0.1.1-604800000',
            'NEXT_LOCALE': 'en',
        }

        headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Accept-Language': 'ru',
            'Sec-Fetch-Mode': 'cors',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://chat.mistral.ai',
            # 'Content-Length': '112',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6.1 Safari/605.1.15',
            'Referer': 'https://chat.mistral.ai/chat/22022363-03fe-4787-a077-4f9db6ef0d09',
            'Connection': 'keep-alive',
            'Host': 'chat.mistral.ai',
            'Sec-Fetch-Dest': 'empty',
            # 'Cookie': 'cc_cookie=%7B%22categories%22%3A%5B%22necessary%22%5D%2C%22revision%22%3A1%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-11-20T19%3A02%3A36.823Z%22%2C%22consentId%22%3A%2212fd04af-4af6-48a3-8531-b7cf317849d1%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22support%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-11-20T19%3A02%3A36.823Z%22%2C%22expirationTime%22%3A1747854156824%7D; csrf_token_1d61ec8f0158ec4868343239ec73dbe1bfebad9908ad860e62f470c767573d0d=6gY50KZbnl2NSUD59+ko1I5hAky72+HN12ht0XeTc1s=; ory_session_coolcurranf83m3srkfl=MTczMjEyOTM0NXx6V1ZmR1NBRW8zYmdBOXQ0dExwS2hZMnhaWW4zRmpHRzdndlo1RUJ2bnY4c1ZOT01ubHNramJKRVlTLUU5NTN3RXpULXpkQWs0STBBQWVBSnJiS0x5blZlSFEwbldRQXBSRjBseVYwWjVSTWhzaHQzdjNmbXhGWlp2LVRFSTQwa0NraEdUZGNocjFXdno0aGRsODRVdWpIbjRMcGFaTVByU0QtdW92b0E2NXhPa3JmeDZIMG9QXzh6Y1ZNMHNyMlYwVjFKVWZwWjVZR3lGWXI2MkJVWVc2TVRyVlNod1BBZno1N2ZIYTFfUG5HX1huSmZISjBkdThuQUxNdzVvRG1kTC1ZczlIUkQ1LTNnVXhzSjB3Vml88Zdm3aoVHYI1BWZT_zv2pC2AAxlr0pfGNFpIopPgrbE=; ory_kratos_continuity=MTczMjEyOTM0MnxEWDhFQVFMX2dBQUJFQUVRQUFCZl80QUFBUVp6ZEhKcGJtY01Jd0FoYjNKNVgydHlZWFJ2YzE5dmFXUmpYMkYxZEdoZlkyOWtaVjl6WlhOemFXOXVCbk4wY21sdVp3d21BQ1F4T1RVM1pqWTRPQzAzWXpnMkxUUTNPVGN0WW1JMU1pMWxZbVJpWW1OaE16QmtZakU9fPLGXdybf2DxKxccQVR7jNKzSWXgVW-ilTeOUWw6goRU; _cfuvid=UeuH605FiAbN7_HEToLsQyQw.T.LhOrDyzuTEHJT6hM-1732129336257-0.0.1.1-604800000; NEXT_LOCALE=en',
            'baggage': 'sentry-environment=production,sentry-release=e06f8a7f90d74b679780e538786f31256c8495f0,sentry-public_key=f45309fe00350c22253424f36dd157d8,sentry-trace_id=3513a895a8f642f2b5c3b2683fa5c063,sentry-sample_rate=0.01,sentry-sampled=false',
            'sentry-trace': '3513a895a8f642f2b5c3b2683fa5c063-ab7089d1c9dc4b70-0',
        }

        json_data = {
            'chatId': chat_id,
            'mode': 'start',
            'clientPromptData': {
                'currentDate': '2024-11-25',
            },
        }

        response = requests.post('https://chat.mistral.ai/api/chat', cookies=cookies, headers=headers, json=json_data)    
        # response.encoding = 'utf-8'

        chunks = response.text.split('\n')
        message = ''
        
        for chunk in chunks:
            if not chunk:
                continue
            try:
                prefix, content = chunk.split(':', 1)
                if prefix == '0':  # Message content
                    message += content.strip('"')
                elif prefix == '1':  # Status
                    continue
            except ValueError:
                continue
                
        return message

    def delete_chat(self, chat_id):
        cookies = {
            'cc_cookie': '%7B%22categories%22%3A%5B%22necessary%22%5D%2C%22revision%22%3A1%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-11-20T19%3A02%3A36.823Z%22%2C%22consentId%22%3A%2212fd04af-4af6-48a3-8531-b7cf317849d1%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22support%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-11-20T19%3A02%3A36.823Z%22%2C%22expirationTime%22%3A1747854156824%7D',
            'csrf_token_1d61ec8f0158ec4868343239ec73dbe1bfebad9908ad860e62f470c767573d0d': '6gY50KZbnl2NSUD59+ko1I5hAky72+HN12ht0XeTc1s=',
            'ory_session_coolcurranf83m3srkfl': 'MTczMjEyOTM0NXx6V1ZmR1NBRW8zYmdBOXQ0dExwS2hZMnhaWW4zRmpHRzdndlo1RUJ2bnY4c1ZOT01ubHNramJKRVlTLUU5NTN3RXpULXpkQWs0STBBQWVBSnJiS0x5blZlSFEwbldRQXBSRjBseVYwWjVSTWhzaHQzdjNmbXhGWlp2LVRFSTQwa0NraEdUZGNocjFXdno0aGRsODRVdWpIbjRMcGFaTVByU0QtdW92b0E2NXhPa3JmeDZIMG9QXzh6Y1ZNMHNyMlYwVjFKVWZwWjVZR3lGWXI2MkJVWVc2TVRyVlNod1BBZno1N2ZIYTFfUG5HX1huSmZISjBkdThuQUxNdzVvRG1kTC1ZczlIUkQ1LTNnVXhzSjB3Vml88Zdm3aoVHYI1BWZT_zv2pC2AAxlr0pfGNFpIopPgrbE=',
            'ory_kratos_continuity': 'MTczMjEyOTM0MnxEWDhFQVFMX2dBQUJFQUVRQUFCZl80QUFBUVp6ZEhKcGJtY01Jd0FoYjNKNVgydHlZWFJ2YzE5dmFXUmpYMkYxZEdoZlkyOWtaVjl6WlhOemFXOXVCbk4wY21sdVp3d21BQ1F4T1RVM1pqWTRPQzAzWXpnMkxUUTNPVGN0WW1JMU1pMWxZbVJpWW1OaE16QmtZakU9fPLGXdybf2DxKxccQVR7jNKzSWXgVW-ilTeOUWw6goRU',
            '_cfuvid': 'UeuH605FiAbN7_HEToLsQyQw.T.LhOrDyzuTEHJT6hM-1732129336257-0.0.1.1-604800000',
            'NEXT_LOCALE': 'en',
        }

        headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Accept-Language': 'ru',
            'Sec-Fetch-Mode': 'cors',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://chat.mistral.ai',
            # 'Content-Length': '60',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6.1 Safari/605.1.15',
            'Referer': 'https://chat.mistral.ai/chat/6443b2b1-64d0-4a28-a15d-76ff7c83f73c',
            'Connection': 'keep-alive',
            'Host': 'chat.mistral.ai',
            'Sec-Fetch-Dest': 'empty',
            # 'Cookie': 'cc_cookie=%7B%22categories%22%3A%5B%22necessary%22%5D%2C%22revision%22%3A1%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-11-20T19%3A02%3A36.823Z%22%2C%22consentId%22%3A%2212fd04af-4af6-48a3-8531-b7cf317849d1%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22support%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-11-20T19%3A02%3A36.823Z%22%2C%22expirationTime%22%3A1747854156824%7D; csrf_token_1d61ec8f0158ec4868343239ec73dbe1bfebad9908ad860e62f470c767573d0d=6gY50KZbnl2NSUD59+ko1I5hAky72+HN12ht0XeTc1s=; ory_session_coolcurranf83m3srkfl=MTczMjEyOTM0NXx6V1ZmR1NBRW8zYmdBOXQ0dExwS2hZMnhaWW4zRmpHRzdndlo1RUJ2bnY4c1ZOT01ubHNramJKRVlTLUU5NTN3RXpULXpkQWs0STBBQWVBSnJiS0x5blZlSFEwbldRQXBSRjBseVYwWjVSTWhzaHQzdjNmbXhGWlp2LVRFSTQwa0NraEdUZGNocjFXdno0aGRsODRVdWpIbjRMcGFaTVByU0QtdW92b0E2NXhPa3JmeDZIMG9QXzh6Y1ZNMHNyMlYwVjFKVWZwWjVZR3lGWXI2MkJVWVc2TVRyVlNod1BBZno1N2ZIYTFfUG5HX1huSmZISjBkdThuQUxNdzVvRG1kTC1ZczlIUkQ1LTNnVXhzSjB3Vml88Zdm3aoVHYI1BWZT_zv2pC2AAxlr0pfGNFpIopPgrbE=; ory_kratos_continuity=MTczMjEyOTM0MnxEWDhFQVFMX2dBQUJFQUVRQUFCZl80QUFBUVp6ZEhKcGJtY01Jd0FoYjNKNVgydHlZWFJ2YzE5dmFXUmpYMkYxZEdoZlkyOWtaVjl6WlhOemFXOXVCbk4wY21sdVp3d21BQ1F4T1RVM1pqWTRPQzAzWXpnMkxUUTNPVGN0WW1JMU1pMWxZbVJpWW1OaE16QmtZakU9fPLGXdybf2DxKxccQVR7jNKzSWXgVW-ilTeOUWw6goRU; _cfuvid=UeuH605FiAbN7_HEToLsQyQw.T.LhOrDyzuTEHJT6hM-1732129336257-0.0.1.1-604800000; NEXT_LOCALE=en',
            'baggage': 'sentry-environment=production,sentry-release=e06f8a7f90d74b679780e538786f31256c8495f0,sentry-public_key=f45309fe00350c22253424f36dd157d8,sentry-trace_id=a7f4785ec19145d6b2c2a97fb4481c20,sentry-sample_rate=0.01,sentry-sampled=false',
            'sentry-trace': 'a7f4785ec19145d6b2c2a97fb4481c20-a8232e9168ee9884-0',
        }

        params = {
            'batch': '1',
        }

        json_data = {
            '0': {
                'json': {
                    'id': chat_id,
                },
            },
        }

        response = requests.post(
            'https://chat.mistral.ai/api/trpc/chat.delete',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
        )
    
    def get_url_to_upload(self):
        cookies = {
            'cc_cookie': '%7B%22categories%22%3A%5B%22necessary%22%5D%2C%22revision%22%3A1%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-11-20T19%3A02%3A36.823Z%22%2C%22consentId%22%3A%2212fd04af-4af6-48a3-8531-b7cf317849d1%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22support%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-11-20T19%3A02%3A36.823Z%22%2C%22expirationTime%22%3A1747854156824%7D',
            'csrf_token_1d61ec8f0158ec4868343239ec73dbe1bfebad9908ad860e62f470c767573d0d': '6gY50KZbnl2NSUD59+ko1I5hAky72+HN12ht0XeTc1s=',
            'ory_session_coolcurranf83m3srkfl': 'MTczMjEyOTM0NXx6V1ZmR1NBRW8zYmdBOXQ0dExwS2hZMnhaWW4zRmpHRzdndlo1RUJ2bnY4c1ZOT01ubHNramJKRVlTLUU5NTN3RXpULXpkQWs0STBBQWVBSnJiS0x5blZlSFEwbldRQXBSRjBseVYwWjVSTWhzaHQzdjNmbXhGWlp2LVRFSTQwa0NraEdUZGNocjFXdno0aGRsODRVdWpIbjRMcGFaTVByU0QtdW92b0E2NXhPa3JmeDZIMG9QXzh6Y1ZNMHNyMlYwVjFKVWZwWjVZR3lGWXI2MkJVWVc2TVRyVlNod1BBZno1N2ZIYTFfUG5HX1huSmZISjBkdThuQUxNdzVvRG1kTC1ZczlIUkQ1LTNnVXhzSjB3Vml88Zdm3aoVHYI1BWZT_zv2pC2AAxlr0pfGNFpIopPgrbE=',
            'ory_kratos_continuity': 'MTczMjEyOTM0MnxEWDhFQVFMX2dBQUJFQUVRQUFCZl80QUFBUVp6ZEhKcGJtY01Jd0FoYjNKNVgydHlZWFJ2YzE5dmFXUmpYMkYxZEdoZlkyOWtaVjl6WlhOemFXOXVCbk4wY21sdVp3d21BQ1F4T1RVM1pqWTRPQzAzWXpnMkxUUTNPVGN0WW1JMU1pMWxZbVJpWW1OaE16QmtZakU9fPLGXdybf2DxKxccQVR7jNKzSWXgVW-ilTeOUWw6goRU',
            '_cfuvid': 'UeuH605FiAbN7_HEToLsQyQw.T.LhOrDyzuTEHJT6hM-1732129336257-0.0.1.1-604800000',
            'NEXT_LOCALE': 'en',
        }

        headers = {
            'Content-Type': 'application/json',
            'Accept': '*/*',
            'Sec-Fetch-Site': 'same-origin',
            'Accept-Language': 'ru',
            'Sec-Fetch-Mode': 'cors',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Origin': 'https://chat.mistral.ai',
            # 'Content-Length': '41',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6.1 Safari/605.1.15',
            'Referer': 'https://chat.mistral.ai/chat/4958b9c8-6a4e-47b0-91a6-45472fe9616c',
            'Connection': 'keep-alive',
            'Host': 'chat.mistral.ai',
            'Sec-Fetch-Dest': 'empty',
            # 'Cookie': 'cc_cookie=%7B%22categories%22%3A%5B%22necessary%22%5D%2C%22revision%22%3A1%2C%22data%22%3Anull%2C%22consentTimestamp%22%3A%222024-11-20T19%3A02%3A36.823Z%22%2C%22consentId%22%3A%2212fd04af-4af6-48a3-8531-b7cf317849d1%22%2C%22services%22%3A%7B%22necessary%22%3A%5B%5D%2C%22analytics%22%3A%5B%5D%2C%22support%22%3A%5B%5D%7D%2C%22lastConsentTimestamp%22%3A%222024-11-20T19%3A02%3A36.823Z%22%2C%22expirationTime%22%3A1747854156824%7D; csrf_token_1d61ec8f0158ec4868343239ec73dbe1bfebad9908ad860e62f470c767573d0d=6gY50KZbnl2NSUD59+ko1I5hAky72+HN12ht0XeTc1s=; ory_session_coolcurranf83m3srkfl=MTczMjEyOTM0NXx6V1ZmR1NBRW8zYmdBOXQ0dExwS2hZMnhaWW4zRmpHRzdndlo1RUJ2bnY4c1ZOT01ubHNramJKRVlTLUU5NTN3RXpULXpkQWs0STBBQWVBSnJiS0x5blZlSFEwbldRQXBSRjBseVYwWjVSTWhzaHQzdjNmbXhGWlp2LVRFSTQwa0NraEdUZGNocjFXdno0aGRsODRVdWpIbjRMcGFaTVByU0QtdW92b0E2NXhPa3JmeDZIMG9QXzh6Y1ZNMHNyMlYwVjFKVWZwWjVZR3lGWXI2MkJVWVc2TVRyVlNod1BBZno1N2ZIYTFfUG5HX1huSmZISjBkdThuQUxNdzVvRG1kTC1ZczlIUkQ1LTNnVXhzSjB3Vml88Zdm3aoVHYI1BWZT_zv2pC2AAxlr0pfGNFpIopPgrbE=; ory_kratos_continuity=MTczMjEyOTM0MnxEWDhFQVFMX2dBQUJFQUVRQUFCZl80QUFBUVp6ZEhKcGJtY01Jd0FoYjNKNVgydHlZWFJ2YzE5dmFXUmpYMkYxZEdoZlkyOWtaVjl6WlhOemFXOXVCbk4wY21sdVp3d21BQ1F4T1RVM1pqWTRPQzAzWXpnMkxUUTNPVGN0WW1JMU1pMWxZbVJpWW1OaE16QmtZakU9fPLGXdybf2DxKxccQVR7jNKzSWXgVW-ilTeOUWw6goRU; _cfuvid=UeuH605FiAbN7_HEToLsQyQw.T.LhOrDyzuTEHJT6hM-1732129336257-0.0.1.1-604800000; NEXT_LOCALE=en',
            'baggage': 'sentry-environment=production,sentry-release=e06f8a7f90d74b679780e538786f31256c8495f0,sentry-public_key=f45309fe00350c22253424f36dd157d8,sentry-trace_id=91a6905dd0404586896b13a0b8706604,sentry-sample_rate=0.01,sentry-sampled=false',
            'sentry-trace': '91a6905dd0404586896b13a0b8706604-ad305d787d500421-0',
        }

        params = {
            'batch': '1',
        }

        json_data = {
            '0': {
                'json': {
                    'type': 'image',
                    'count': 1,
                },
            },
        }

        response = requests.post(
            'https://chat.mistral.ai/api/trpc/file.uploadFile',
            params=params,
            cookies=cookies,
            headers=headers,
            json=json_data,
        )   

        return response.json()[0]['result']['data']['json']['uploadURLs'][0]

    def upload_file(self, url, file_path):
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Access-Control-Request-Headers': 'content-type,x-ms-blob-type,x-ms-client-request-id,x-ms-useragent,x-ms-version',
            'Access-Control-Request-Method': 'PUT',
            'Connection': 'keep-alive',
            'Origin': 'https://chat.mistral.ai',
            'Referer': 'https://chat.mistral.ai/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
        }

        params = {
            'sv': '2024-11-04',
            'st': '2024-11-26T08:49:50Z',
            'se': '2024-11-26T08:59:50Z',
            'sr': 'b',
            'sp': 'racte',
            'sig': 'f1Krp5uVQWJ2Z6MWU+9pctDyFLSnTQdFP3Aj4je3H04=',
        }

        response = requests.options(
            'https://mistralaichatupprodswe.blob.core.windows.net/chat-images/17/3d/d3/173dd3bc-0a4a-4917-92d7-130b7f83335a/e4df1aaa-2c99-486b-ad96-9044c650db02/9c671ba7-dadc-4471-91ab-ef61e8b453b9',
            params=params,
            headers=headers,
        )

        print(response.status_code)
        print(response.text)

        headers = {
            'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Origin': 'https://chat.mistral.ai',
            'Referer': 'https://chat.mistral.ai/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'cross-site',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36',
            'accept': 'application/xml',
            'content-type': 'application/octet-stream',
            'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'x-ms-blob-type': 'BlockBlob',
            'x-ms-client-request-id': '6f621ece-fe41-40ff-b208-812379feced2',
            'x-ms-useragent': 'azsdk-js-azure-storage-blob/12.25.0 core-rest-pipeline/1.17.0 Google Chrome/131 OS/x86-Windows-10.0.0',
            'x-ms-version': '2024-11-04'
        }

        # params = {
        #     'sv': '2024-11-04',
        #     'st': '2024-11-26T08:49:50Z',
        #     'se': '2024-11-26T08:59:50Z',
        #     'sr': 'b',
        #     'sp': 'racte',
        #     'sig': 'f1Krp5uVQWJ2Z6MWU+9pctDyFLSnTQdFP3Aj4je3H04=',
        # }

        with open(file_path, 'rb') as f:
            # data = str(f.read())[1:]
            data = f.read()

        response = requests.put(
            url=url,
            headers=headers,
            data=data,
        )

        print(response.status_code)
        print(response.text)

    def generate(self, promt, file=None):
        file_url = None
        if file:
            file_url = self.get_url_to_upload()
            self.upload_file(file_url, file)

        chat_id = self.create_chat(promt=promt, file_url=file_url, filename=file)

        print(chat_id)

        message = self.start_new_chat(chat_id)
        self.delete_chat(chat_id)

        return message



if __name__ == "__main__":
    individual_parameters = (f'Год рождения: 30.01.2008\n'
                            f'Пол: м\n'
                            f'Рост: 182\n'
                            f'Вес: 69\n'
                            f'Цель: Нарастить мышцы\n'
                            f'Опыт: Никогда\n')
                            
    llm = MistralLLM()
    response = llm.generate(config.GENERATE_PLAN_PROMT + f'\n{individual_parameters}')
    print(response)