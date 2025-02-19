import requests

# URL для получения цен на пары
url = "https://api.binance.com/api/v3/ticker/price"

# Отправляем GET-запрос
response = requests.get(url)

# Проверяем успешность запроса
if response.status_code == 200:
    # Получаем данные в формате JSON
    prices = response.json()
    
    # Выводим символы (пары) и цены первых 5 элементов
    print("Первые 5 торговых пар и их цены:")
    for i, price_data in enumerate(prices[:5], start=1):
        symbol = price_data['symbol']
        price = price_data['price']
        print(f"{i}. Пара: {symbol}, Цена: {price}")
else:
    print(f"Ошибка при получении данных. Код ошибки: {response.status_code}")