import requests
import pandas as pd
from dotenv import load_dotenv
import os
import json
import re

load_dotenv()

API_KEY = os.getenv('NEWS_API_KEY')
URL = os.getenv('NEWS_API_URL')

query = ( 
    '"EUR/USD" OR "USD/EUR" OR "euro dollar" OR "foreign exchange" OR '
    '"currency markets" OR "exchange rate" OR "interest rate" OR '
    '"ECB" OR "Federal Reserve" OR "Fed" OR "monetary policy" OR '
    '"inflation" OR "GDP" OR "unemployment" OR "PMI" OR "economic outlook" OR '
    '"geopolitical risk" OR "trade war" OR "fiscal policy" OR "rate hike" OR "rate cut"'
    )

params = {
    'q': query,
    'language': 'en',
    'sortBy': 'publishedAt',
    # 'from': '2010-01-01',  # need to upgrade to a paid plan to get older data
    # 'to': '2023-12-13',
    'apiKey': API_KEY
}


response = requests.get(URL, params=params)

# Parse the JSON and remove unreadable characters by decoding properly
try:
    data = response.json()
except json.JSONDecodeError:
    print("Failed to decode JSON")
    data = {}

# Save the JSON with formatting
cleaned_query = re.sub(r'"(.*?)"', r"'\1'", query)
output = {
    'query': cleaned_query,
    'response': data
}
with open('../../data/external/news_api_detailed_query.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, indent=4, ensure_ascii=False)

articles = data.get('articles', [])
print(f"Number of articles: {len(articles)}")