import os
import json
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# List your JSON files here
json_files = [
    "../../data/external/api_responses/realtime_news_full_story_20250515_124224.json",
    "../../data/external/api_responses/realtime_news_search_20250515_124219.json",
    "../../data/external/api_responses/realtime_news_topic_20250515_124222.json",
]

base_output_dir  = "../../data/external/scraped/realtime_news"
os.makedirs(base_output_dir , exist_ok=True)

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}


def get_article_text(url):
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"Failed to retrieve {url} (status code {response.status_code})")
            return None
        soup = BeautifulSoup(response.content, "html.parser")
        paragraphs = soup.find_all("p")
        text = "\n\n".join(p.get_text() for p in paragraphs if p.get_text())
        return text.strip()
    except Exception as e:
        print(f"Error while scraping {url}: {e}")
        return None

def url_to_path(url, cov = None):
    parsed = urlparse(url)
    netloc = parsed.netloc
    path_parts = parsed.path.strip("/").split("/")
    if path_parts[-1] == "":
        path_parts = path_parts[:-1]
    # handle when url ends with .html or similar
    if path_parts and path_parts[-1].endswith(('.html', '.htm', '.php')):
        path_parts[-1] = path_parts[-1].rsplit('.', 1)[0]  # remove extension

    filename = path_parts[-1] + ".txt" if path_parts else "index.txt"
    dir_path = os.path.join(*base_output_dir.split('/'), cov, netloc, *path_parts[:-1])
    return os.path.join(dir_path, filename)

# Unified URL extractor
def extract_urls(api_response, file_name):
    urls = []

    # realtime data format (check for "data" and "OK")
    status = api_response.get("status", "")
    data = api_response.get("data", {})
    if status == "OK" :
        for entry in data if isinstance(data, list) else data.get("all_articles", []): # handled for full news difference
            url = entry["link"]
            if url:
                urls.append(url)
    else:
        print(f"Unrecognized format in file: {file_name}")

    return urls

# Process all files
for json_file in json_files:
    print(f"\nProcessing {json_file}...")
    with open(json_file, "r", encoding="utf-8") as f:
        try:
            api_response = json.load(f)
        except json.JSONDecodeError:
            print(f"Failed to parse {json_file}, skipping.")
            continue
    
    urls = extract_urls(api_response, json_file)
    cov = json_file.split("_")[3]
    print(f"working on {cov}")
    for url in urls:
        article_text = get_article_text(url)
        if not article_text:
            continue

        full_path = url_to_path(url, cov)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        try:
            with open(full_path, "w", encoding="utf-8") as f:
                f.write(article_text)
                print(f"Saved: {full_path}")
        except Exception as e:
            print(f"Failed to save {full_path}: {e}")
            continue