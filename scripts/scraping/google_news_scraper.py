import os
import json
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


# List your JSON files here
json_files = [
    "C:/Users/bemne/Documents/projects/fmp/data/external/api_responses/google_news_v13_business_20250515_124213.json",
    "C:/Users/bemne/Documents/projects/fmp/data/external/api_responses/google_news_v13_technology_20250515_124213.json",
    "C:/Users/bemne/Documents/projects/fmp/data/external/api_responses/google_news_v22_20250515_124215.json",
]

base_output_dir  = "C:/Users/bemne/Documents/projects/fmp/data/external/articles/google_news"
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

def url_to_path(url):
    parsed = urlparse(url)
    netloc = parsed.netloc
    path_parts = parsed.path.strip("/").split("/")
    if path_parts[-1] == "":
        path_parts = path_parts[:-1]
    filename = path_parts[-1] + ".txt" if path_parts else "index.txt"
    dir_path = os.path.join(base_output_dir, netloc, *path_parts[:-1])
    return os.path.join(dir_path, filename)

# Unified URL extractor
def extract_urls(api_response, file_name):
    urls = []

    # Version 22 format (check for "data" and "success")
    if "success" in api_response and "data" in api_response:
        for entry in api_response["data"]:
            url = entry.get("url")
            if url:
                urls.append(url)
    # Original format (with "items" and "subnews")
    elif "items" in api_response:
        for item in api_response["items"]:
            for sub in item.get("subnews", []):
                url = sub.get("newsUrl")
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

    for url in urls:
        article_text = get_article_text(url)
        if not article_text:
            continue

        full_path = url_to_path(url)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(article_text)
            print(f"Saved: {full_path}")