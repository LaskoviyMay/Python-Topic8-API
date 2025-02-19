import requests

# API ключ от OpenWeatherMap
API_KEY = "bd5e378503939ddaee76f12ad7a97608"  # API ключ
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Функция для получения погоды
def get_weather(city):
    # Параметры запроса
    params = {
        "q": city,  # Название города
        "appid": API_KEY,  # API ключ
        "units": "metric",  # Температура в градусах Цельсия
        "lang": "ru"  # Язык описания погоды (русский)
    }

    # Отправляем GET-запрос
    response = requests.get(BASE_URL, params=params)

    # Проверяем успешность запроса
    if response.status_code == 200:
        data = response.json()
        # Извлекаем данные о температуре и описании погоды
        temperature = data["main"]["temp"]
        weather_description = data["weather"][0]["description"]
        print(f"Текущая погода в {city}:")
        print(f"Температура: {temperature}°C")
        print(f"Описание: {weather_description.capitalize()}")
    else:
        print(f"Ошибка при получении данных. Код ошибки: {response.status_code}")
        print("Пожалуйста, проверьте название города.")

if __name__ == "__main__":
    city = input("Введите название города: ")
    get_weather(city)