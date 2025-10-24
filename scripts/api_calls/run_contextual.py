import os
import json
from datetime import datetime
from dotenv import load_dotenv

from contextualweb_fetch import (
    fetch_real_time_cash_flow,
    fetch_google_news,
    fetch_reuters_news,
    fetch_forex_factory,
    fetch_news_data
)


load_dotenv()

OUTPUT_DIR = "../../data/external/api_responses"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def save_json_response(data, name):
    if not data:
        print(f"[WARNING] No data to save for: {name}")
        return
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(OUTPUT_DIR, f"{name}_{timestamp}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    print(f"[SAVED] {file_path}")


def wrapped_fetch_real_time_cash_flow():
    api_url = os.getenv("REALTIME_FINANCE_API_URL")
    api_host = os.getenv("REALTIME_FINANCE_API_HOST")
    api_key = os.getenv("RAPIDAPI_KEY")

    response = fetch_real_time_cash_flow(api_url, api_host, api_key)
    if response:
        save_json_response(response, "real_time_cash_flow")


def wrapped_fetch_google_news(version, search=None):
    if version == 13:
        api_url = os.getenv("GOOGLE_NEWS13_API_URL")
        api_host = os.getenv("GOOGLE_NEWS13_API_HOST")
        if search == 'business':
            api_url = os.getenv("GOOGLE_NEWS13_API_URL_BUSINESS")
        if search == 'technology':
            api_url = os.getenv("GOOGLE_NEWS13_API_URL_TECHNOLOGY")

    elif version == 22:
        api_url = os.getenv("GOOGLE_NEWS22_API_URL")
        api_host = os.getenv("GOOGLE_NEWS22_API_HOST")
    else:
        return

    api_key = os.getenv("RAPIDAPI_KEY")

    response = fetch_google_news(api_url, api_host, api_key, version=version)
    version_str = f"v{version}_{search}" if search else f"v{version}"
    if response:
        save_json_response(response, f"google_news_{version_str}")


def wrapped_fetch_reuters_news():
    api_url = os.getenv("REUTERS_API_URL")
    api_host = os.getenv("REUTERS_API_HOST")
    api_key = os.getenv("RAPIDAPI_KEY")

    response = fetch_reuters_news(api_url, api_host, api_key)
    if response:
        save_json_response(response, "reuters_news")


def wrapped_fetch_forex_factory():
    api_url = os.getenv("FOREX_FACTORY_SCRAPER_API_URL")
    api_host = os.getenv("FOREX_FACTORY_SCRAPER_API_HOST")
    api_key = os.getenv("RAPIDAPI_KEY")

    response = fetch_forex_factory(api_url, api_host, api_key)
    if response:
        save_json_response(response, "forex_factory")


def wrapped_fetch_realtime_news_topic():
    # Uses 3 URLs inside
    api_key = os.getenv("RAPIDAPI_KEY")
    api_host = os.getenv("REALTIME_NEWS_API_HOST")

    # Save each request manually
    urls = {
        "search": "https://real-time-news-data.p.rapidapi.com/search?query=tariff&limit=10&time_published=anytime&lang=en",
        "topic": "https://real-time-news-data.p.rapidapi.com/topic-headlines?topic=WORLD&limit=500&country=US&lang=en",
        "full_story": "https://real-time-news-data.p.rapidapi.com/full-story-coverage?story=CAAqKAgKIiJDQkFTRXdvTkwyY3ZNVEZ5YTJKNFpEUXlYeElDWlc0b0FBUAE&sort=RELEVANCE"
    }


    for name, url in urls.items():
        response = fetch_news_data(url, api_host, api_key)
        if response:
            save_json_response(response, f"realtime_news_{name}")


# ========== Run All ==========
if __name__ == "__main__":
    wrapped_fetch_real_time_cash_flow()
    wrapped_fetch_google_news(version=13, search='business')
    wrapped_fetch_google_news(version=13, search='technology')
    wrapped_fetch_google_news(version=22)
    wrapped_fetch_reuters_news()
    wrapped_fetch_forex_factory()
    wrapped_fetch_realtime_news_topic()
