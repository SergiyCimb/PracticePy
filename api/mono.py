import requests
def get_currency_rate(currency_code_a=840, currency_code_b=980):
    url = "https://api.monobank.ua/bank/currency"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for item in data:
            if item['currencyCodeA'] == currency_code_a and item['currencyCodeB'] == currency_code_b:
                rate = item.get('rateCross') or item.get('rateBuy')
                print(f"Курс: {currency_code_a}/{currency_code_b} = {rate}")
                return rate
        print("Валюта не знайдена.")
    else:
        print("Помилка при запиті до API:", response.status_code)
get_currency_rate(840, 980)