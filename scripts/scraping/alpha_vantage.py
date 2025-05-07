import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('ALPHA_VANTAGE_API_KEY')
URL = os.getenv('ALPHA_VANTAGE_API_URL')

params = {
    'function': 'CURRENCY_EXCHANGE_RATE',
    'from_currency': 'USD',
    'to_currency': 'EUR',
    'apikey': API_KEY
}

response = requests.get(URL, params=params)
data = response.json()
exchange_rate = data['Realtime Currency Exchange Rate']['5. Exchange Rate']

print("Current USD/EUR exchange rate:", exchange_rate)
