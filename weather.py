import requests


def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {"key": "f4feafc05c2c4c36b41105301240206",
              "q": city_name,
              "num_of_day": 1,
              "lang": "ru",
              "format": "json",
              }
    result = requests.get(weather_url, params=params)
    weather = result.json()
    if "data" in weather:
        if "current_condition" in weather["data"]:
            try:
                return weather["data"]["current_condition"][0]
            except (IndexError, TypeError):
                return False
    return weather


if __name__ == "__main__":
    print(weather_by_city("Moscow, Russia"))

