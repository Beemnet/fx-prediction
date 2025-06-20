import feedparser
import json
import os
from dotenv import load_dotenv

load_dotenv()

# RSS URLs from environment variables
rss_sources = {
    "ecb_press_releases": os.getenv("ECB_PRESS_RSS_URL"),
    "ecb_publications": os.getenv("ECB_PUBLICATIONS_RSS_URL"),
    "ecb_statistical_press_releases": os.getenv("ECB_STATS_RSS_URL"),
    "ecb_open_market_operations": os.getenv("ECB_OMO_RSS_URL")
}

# Directory to save feeds
output_dir = "../../data/external/ecb_rss_feed"
os.makedirs(output_dir, exist_ok=True)

# Process each RSS feed
for name, url in rss_sources.items():
    if not url:
        print(f"[WARNING] URL for {name} is not set in .env.")
        continue

    print(f"[ECB RSS] Fetching {name.replace('_', ' ').title()} from: {url}")
    feed = feedparser.parse(url)

    summary = feed["feed"]["summary"] if "summary" in feed["feed"] else None
    if summary:
        summary_output_path = os.path.join(output_dir, f"{name}_summary.json")
        with open(summary_output_path, "w", encoding="utf-8") as f:
            json.dump(summary, f, indent=4, ensure_ascii=False)
        feed["feed"]["summary"] = f"Located in {os.path.abspath(summary_output_path)}"

    output_path = os.path.join(output_dir, f"{name}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(feed, f, indent=4, ensure_ascii=False, default=str)

    print(f"[ECB RSS] Saved {name} to {os.path.abspath(output_path)}")
