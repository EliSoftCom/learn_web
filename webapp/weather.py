import requests


def weather_by_city(city_name):
    weather_url = "http://api.worldweatheronline.com/premium/v1/weather.ashx"
    params = {"key": "f4feafc05c2c4c36b41105301240206",
              "q": city_name,
              "num_of_day": 1,
              "lang": "ru",
              "format": "json",
              }
    try:
        result = requests.get(weather_url, params=params)
        result.raise_for_status()
        weather = result.json()
        if "data" in weather:
            if "current_condition" in weather["data"]:
                try:
                    return weather["data"]["current_condition"][0]
                except (IndexError, TypeError):
                    return False
    except (requests.RequestException, ValueError):
        print("Сетевая ошибка")
        return False
    return False


if __name__ == "__main__":
    print(weather_by_city("Moscow, Russia"))

