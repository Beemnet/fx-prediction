import feedparser
import json
import os
import re
import urllib.parse
from dotenv import load_dotenv

load_dotenv()

# Base URL for Google News RSS
GOOGLE_RSS_URL = os.getenv("GOOGLE_RSS_URL")

# List of search queries relevant to EUR/USD
search_terms = [
    "EUR USD",
    "ECB interest rates",
    "Federal Reserve",
    "inflation eurozone",
    "geopolitical tensions",
    "economic forecast Europe",
    "USD strength"
    '"monetary policy" euro',
    '"interest rate policy" ECB',
    '"central bank policy" eurozone',
    'inflation euro',
    '"consumer price index" eurozone',
    'CPI ECB',
    '"price stability" EU',
    '"ECB decision" euro',
    '"ECB announcement" euro',
    '"ECB meeting" euro',
    '"Governing Council" ECB',
    '"interest rate hike" ECB',
    '"rate cut" ECB',
    '"EUR/USD" inflation',
    '"euro dollar exchange rate" "interest rate"',
    '"ECB policy" "quantitative easing"',
    '"monetary tightening" euro'
]

# Output directory
output_dir = "../../data/external/google_news_rss"
os.makedirs(output_dir, exist_ok=True)

# Function to build the full RSS URL from a search query
def build_google_news_rss_url(query: str) -> str:
    encoded_query = urllib.parse.quote_plus(query)
    return f"{GOOGLE_RSS_URL}?q={encoded_query}&hl=en-US&gl=US&ceid=US:en"

# Process each search term
for term in search_terms:
    rss_url = build_google_news_rss_url(term)
    print(f"[Google News RSS] Fetching '{term}' from: {rss_url}")
    
    feed = feedparser.parse(rss_url)

    # Clean file name
    term = re.sub(r'[<>:"/\\|?*]', '', term)  # Remove invalid characters
    filename = f"{term.lower().replace(' ', '_')}.json"
    output_path = os.path.join(output_dir, filename)

    # Save feed to JSON
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(feed, f, indent=4, ensure_ascii=False, default=str)

    print(f"[Google News RSS] Saved '{term}' feed to {os.path.abspath(output_path)}")
