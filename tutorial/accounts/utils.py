import jwt 
from datetime import datetime, timedelta
from django.conf import settings
import random 
import string

def get_random(length):
    return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))
#이거뭐지

def get_access_token(payload):
    return jwt.encode(
        {"exp":datetime.now() + timedelta(minutes=5),**payload},
        settings.SECRET_KEY,
        algorithm="HS256",
    )

def get_refresh_token():
    return jwt.encode(
        {"exp":datetime.now() + timedelta(minutes=5),"data":get_random(10)},
        settings.SECRET_KEY,
        algorithm="HS256",
    )