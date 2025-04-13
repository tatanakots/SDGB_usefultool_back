import json
import pytz

from sdgb import sdgb_api
from datetime import datetime

from settings import regionId, clientId, placeId

def login(userId, timestamp):
    data = json.dumps({
        "userId": int(userId),
        "accessCode": "",
        "regionId": regionId,
        "placeId": placeId,
        "clientId": clientId,
        "dateTime": timestamp,
        "isContinue": False,
        "genericFlag": 0,
    })

    login_result = sdgb_api(data, "UserLoginApi", int(userId))
    return json.loads(login_result)

def logout(userId, timestamp):
    data = json.dumps({
        "userId": int(userId),
        "accessCode": "",
        "regionId": regionId,
        "placeId": placeId,
        "clientId": clientId,
        "dateTime": timestamp,
        "type": 1
    })

    logout_result = sdgb_api(data, "UserLogoutApi", int(userId))
    return json.loads(logout_result)