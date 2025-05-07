import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_real_time_cash_flow(api_url, api_host, api_key):
    headers = {
        "x-rapidapi-host": api_host,
        "x-rapidapi-key": api_key
    }

    print(f"\n[Real-Time Finance Data] Requesting: {api_url}")
    response = requests.get(api_url, headers=headers)
    
    if response.status_code != 200:
        print(f"Failed to fetch data: {response.status_code} - {response.text}")
        return

    data = response.json()

    # Basic output validation
    if data.get("status") != "OK":
        print("Error in response:", data)
        return

    symbol = data["data"].get("symbol", "N/A")
    period = data["data"].get("period", "N/A")
    cash_flows = data["data"].get("cash_flow", [])

    print(f"\nCash Flow for {symbol} [{period}]")
    for entry in cash_flows[:5]:  # Show first 5 entries
        print(f"Date: {entry['date']}")
        print(f"  Net Income: {entry.get('net_income')}")
        print(f"  Free Cash Flow: {entry.get('free_cash_flow')}")
        print(f"  Cash from Ops: {entry.get('cash_from_operations')}")
        print(f"  Net Change in Cash: {entry.get('net_change_in_cash')}")
        print("")

def fetch_google_news(api_url, api_host, api_key, version=None):
    headers = {
        "x-rapidapi-host": api_host,
        "x-rapidapi-key": api_key
    }

    print(f"\n[Google News {version}] Requesting: {api_url}")
    response = requests.get(api_url, headers=headers)

    if response.status_code != 200:
        print("Request failed:", response.status_code, response.text)
        return

    data = response.json()
    if not data.get("success"):
        print("API returned error:", data)
        return

    articles = data.get("data", [])
    print(f"\nFound {len(articles)} articles. First 3:")
    for article in articles[:3]:
        print(f"- {article['title']}")
        print(f"  {article['url']}")
        print(f"  Source: {article['source']['name']}\n")

def fetch_reuters_news(api_url, api_host, api_key):
    headers = {
        "x-rapidapi-host": api_host,
        "x-rapidapi-key": api_key
    }

    print(f"\n[Reuters News] Requesting: {api_url}")
    response = requests.get(api_url, headers=headers)

    if response.status_code != 200:
        print("Request failed:", response.status_code, response.text)
        return

    try:
        data = response.json()
        print("\nResponse JSON loaded successfully. Showing preview:")
        print(data)
    except Exception as e:
        print("Failed to parse JSON. Raw response:")
        print(response.text)

def fetch_forex_factory(api_url, api_host, api_key):
    headers = {
        "x-rapidapi-host": api_host,
        "x-rapidapi-key": api_key
    }

    print(f"\n[Forex Factory] Requesting: {api_url}")
    response = requests.get(api_url, headers=headers)

    if response.status_code != 200:
        print("Request failed:", response.status_code, response.text)
        return

    data = response.json()
    if not isinstance(data, list):
        print("Unexpected response format:", data)
        return

    print(f"\nFound {len(data)} economic events. First 3:")
    for event in data[:3]:
        print(f"{event['currency']} - {event['name']} at {event['time']} on {event['date']}")
        print(f"  Impact: {event['impact']}, Actual: {event['actual']}, Forecast: {event['forecast']}")
        print("")

def fetch_news_data(api_url, api_host, api_key):
    headers = {
        "x-rapidapi-host": api_host,
        "x-rapidapi-key": api_key
    }

    print(f"\n[News API] Requesting: {api_url}")
    response = requests.get(api_url, headers=headers)
    
    if response.status_code != 200:
        print(f"Request failed: {response.status_code} - {response.text}")
        return

    data = response.json()

    if data.get("status") != "OK":
        print("API returned error:", data)
        return

    # Handle different response formats
    if isinstance(data["data"], list):
        # For /search
        articles = data["data"]
    elif isinstance(data["data"], dict):
        # For /topic-headlines or /full-story-coverage
        articles = data["data"].get("top_news", [])
    else:
        print("Unexpected response format.")
        return

    print(f"\nArticles (showing {min(len(articles), 5)}):")
    for article in articles[:5]:
        print(f"Title: {article.get('title')}")
        print(f"Published: {article.get('published_datetime_utc', 'N/A')}")
        print(f"Source: {article.get('source_name', 'N/A')}")
        print(f"URL: {article.get('link')}\n")

def call_fetch_topic_news(api_key, api_host):

    # 1. Search by keyword
    search_url = "https://real-time-news-data.p.rapidapi.com/search?query=tariff&limit=10&time_published=anytime&lang=en"
    fetch_news_data(search_url, api_host, api_key)

    # 2. Topic headlines (WORLD)
    topic_url = "https://real-time-news-data.p.rapidapi.com/topic-headlines?topic=WORLD&limit=500&country=US&lang=en"
    fetch_news_data(topic_url, api_host, api_key)

    # 3. Full story coverage (sample story ID — replace dynamically later)
    story_id = "CAAqKAgKIiJDQkFTRXdvTkwyY3ZNVEZ5YTJKNFpEUXlYeElDWlc0b0FBUAE"  # I don't know how to get this to work yet
    if story_id:
        full_story_url = f"https://real-time-news-data.p.rapidapi.com/full-story-coverage?story={story_id}&sort=RELEVANCE"
        fetch_news_data(full_story_url, api_host, api_key)


# === Example call ===
if __name__ == "__main__":
    api_key = os.getenv("RAPIDAPI_KEY")
    
    # real time cash flow ---
    # api_url = os.getenv("REALTIME_FINANCE_API_URL")
    # api_host = os.getenv("REALTIME_FINANCE_API_HOST")
    # fetch_real_time_cash_flow(api_url, api_host, api_key)
    # --- 

    # google news, 2 different verions, 2 queries --- 
    # api_url = os.getenv("GOOGLE_NEWS22_API_URL")
    # api_host = os.getenv("GOOGLE_NEWS22_API_HOST")
    # api_url = os.getenv("GOOGLE_NEWS13_API_URL")
    # api_host = os.getenv("GOOGLE_NEWS13_API_HOST")

    # fetch_google_news(api_url, api_host, api_key, version=13)
    # ---

    # reuters news NOT SUBSCRIBED---
    # api_url = os.getenv("REUTERS_API_URL")
    # api_host = os.getenv("REUTERS_API_HOST")
    # fetch_reuters_news(api_url, api_host, api_key)
    # ---


    # topic news (realtime news data) ---
    # api_url = os.getenv("REALTIME_NEWS_API_URL")
    # api_host = os.getenv("REALTIME_NEWS_API_HOST")
    # call_fetch_topic_news(api_key=api_key, api_host=api_host)
    # ---

    # forex factory [IMPORTANT]---
    api_url = os.getenv("FOREX_FACTORY_SCRAPER_API_URL")
    api_host = os.getenv("FOREX_FACTORY_SCRAPER_API_HOST")
    fetch_forex_factory(api_url, api_host, api_key)   
