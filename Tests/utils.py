from django.conf import settings
import requests


def send_sms(phone_number, message):
    api_key = getattr(settings, 'KAVENEGAR_API_KEY')

    if api_key == 'test':
        print(f"[✅ شبیه‌سازی ارسال] پیامک به {phone_number}:")
        print(f"📨 {message}")
        return {'status': 'simulated', 'to': phone_number, 'message': message}

    # از خط فعال خودت استفاده کن
    # sender_line = '0018018949161'

    url = f"https://api.kavenegar.com/v1/{api_key}/sms/send.json"
    params = {
        'receptor': phone_number,
        'message': message,
        # 'sender': sender_line
    }

    try:
        response = requests.get(url, params=params)
        print("send status : ", response.status_code)
        print(" full response : ", response.json())
        return response.json()
    except Exception as e:
        return {'status': 'error', 'detail': str(e)}

