from fastapi import FastAPI, HTTPException, Query
import requests
app = FastAPI()
def fetch_currency_data():
    url = "https://api.monobank.ua/bank/currency"
    response = requests.get(url)
    if response.status_code != 200:
        raise HTTPException(status_code=502, detail="Не вдалося отримати дані з Monobank")
    return response.json()
@app.get("/currency")
def get_currency(currency_from: int = Query(..., description="Код валюти, з якої обмін (наприклад, 840 для USD)"),
                 currency_to: int = Query(..., description="Код валюти, в яку обмін (наприклад, 980 для UAH)")):
    data = fetch_currency_data()
    for item in data:
        if item["currencyCodeA"] == currency_from and item["currencyCodeB"] == currency_to:
            return {
                "from": currency_from,
                "to": currency_to,
                "rateBuy": item.get("rateBuy"),
                "rateSell": item.get("rateSell"),
                "rateCross": item.get("rateCross")
            }
    raise HTTPException(status_code=404, detail="Валютну пару не знайдено")
# Запуск серверу: uvicorn fast_api:app --reload
# Запит через браузер: http://127.0.0.1:8000/currency?currency_from=840&currency_to=980