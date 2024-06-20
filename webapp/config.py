import os

basedir = os.path.abspath(os.path.dirname(__file__))


WEATHER_DEFAULT_CITY = "Roston na Donu,Russia"
WEATHER_API_KEY = "f4feafc05c2c4c36b41105301240206"
WEATHER_URL = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
SQLALCHEMY_DATABASE_URI ='sqlite:///' + os.path.join(basedir, '..', 'webapp.db')