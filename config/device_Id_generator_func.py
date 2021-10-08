import requests
import random
import string
import json

def generate_captcha():
	value = "".join(random.choices(string.ascii_uppercase + string.ascii_lowercase + "_-", k=462)).replace("--", "-")
	return value

def auth(email: str = None, phone: str = None, password: str = None):
        data = {
            "auth_type": 0,
            "recaptcha_challenge": generate_captcha(),
            "recaptcha_version": "v3",
            "secret": password
        }
        if email:
            data["email"] = email
        elif phone:
            data["phoneNumber"] = phone
        request = requests.post("https://aminoapps.com/api/auth", json=data)
        return request.json()
