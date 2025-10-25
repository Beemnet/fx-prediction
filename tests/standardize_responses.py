import pytest
import json
import sys
from datetime import datetime
from pathlib import Path

# sys.path.append(str(Path(__file__).resolve().parents[1]) / "scripts")
from scripts.api_calls.standardize_responses import NewsItem

# TODO: define good expectations validation checks for each entry

SAMPLES_DIR = Path(__file__).parent / "samples"

def load_sample(filename):
    path = SAMPLES_DIR / filename
    with open(path, "r", encoding='utf-8') as f:
        data = json.load(f)
        return data

# sample api data fixtures
@pytest.fixture
def google_v13_item():
    return (load_sample("google_news_v13_sample.json"))

@pytest.fixture
def google_v22_item():
    return {load_sample("google_news_v22_sample.json")}

@pytest.fixture
def realtime_topic_item():
    return {load_sample("realtime_topic_sample.json")}

@pytest.fixture
def realtime_fullstory_item():
    return {load_sample("realtime_fullstory_sample.json")}

# tests

def test_from_google_v13(google_v13_item):
    # obj = NewsItem.from_google_v13(google_v13_item)
    # print(str(obj.to_dict()))
    
    # assert obj.source == "google_news_v13"
    # assert isinstance(obj.to_dict(), dict)

    news_items = NewsItem.from_google_v13(google_v13_item)

    assert isinstance(news_items, list)
    assert len(news_items) > 0

    first = news_items[0] # only check first for test

    assert isinstance(first, NewsItem)
    assert first.source in ("google_news_v13", "google_news_v13_sub")
    assert isinstance(first.to_dict(), dict)
    assert "title" in first.to_dict()
    assert "url" in first.to_dict()
    assert "published_at" in first.to_dict()




