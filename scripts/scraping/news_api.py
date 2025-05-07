import requests
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()


API_KEY = os.getenv('NEWS_API_KEY')
URL = os.getenv('NEWS_API_URL')

params = {
    'q': '"USD EUR" OR "euro dollar"',  # You can expand this
    'language': 'en',
    'sortBy': 'publishedAt',
    'apiKey': API_KEY
}

response = requests.get(URL, params=params)
data = response.json()

# Convert to DataFrame for easier viewing
articles = pd.DataFrame(data['articles'])[['publishedAt', 'title', 'url']]
print(articles.head())
