import requests
import os
import json
from dotenv import load_dotenv
from datetime import datetime

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

rate_data = data.get('Realtime Currency Exchange Rate', {})

# Extract relevant values
meta_fields = {
    '1. From_Currency Code': rate_data.get('1. From_Currency Code'),
    '2. From_Currency Name': rate_data.get('2. From_Currency Name'),
    '3. To_Currency Code': rate_data.get('3. To_Currency Code'),
    '4. To_Currency Name': rate_data.get('4. To_Currency Name')
}

log_fields = {
    'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
    '5. Exchange Rate': rate_data.get('5. Exchange Rate'),
    '6. Last Refreshed': rate_data.get('6. Last Refreshed'),
    '7. Time Zone': rate_data.get('7. Time Zone'),
    '8. Bid Price': rate_data.get('8. Bid Price'),
    '9. Ask Price': rate_data.get('9. Ask Price')
}

output_path = '../../data/external/alpha_vantage_exchange_rate_log.json'

# Check if file exists
if os.path.exists(output_path):
    # Load existing file and append to log
    with open(output_path, 'r', encoding='utf-8') as f:
        existing_data = json.load(f)

    existing_data['log'].append(log_fields)

else:
    # Create new file with metadata and first log entry
    existing_data = {
        'meta': meta_fields,
        'log': [log_fields]
    }

# Write updated data back to file
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(existing_data, f, indent=4, ensure_ascii=False)

# Optional: print to console
print("Current USD/EUR exchange rate:", log_fields['5. Exchange Rate'])
