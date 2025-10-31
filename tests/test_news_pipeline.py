import pytest
import pandas as pd
import json
from scripts.data_pipeline.news_pipeline import NewsPipeline
from scripts.data_pipeline.forex_loader import ForexLoader
from scripts.api_calls.standardize_responses import NewsItem
from pathlib import Path


class MockGDELTClient:
    def query(self, keywords, start, end):
        # return [{"title": "ECB raises rates", "url": "https://example.com", "timestamp": "1735689600000"}]

        # load our fixture file
        p = Path(__file__).parent / "fixtures" / "gdelt_sample.json"
        data = json.loads(p.read_text(encoding="utf-8"))
        return data.get('items', data)

class MockArchiveClient:
    def fetch_text(self, url):
        return "ECB raises rates to combat inflation."
    

@pytest.fixture
def pipeline():
    # loader = ForexLoader()
    return NewsPipeline(MockGDELTClient(), MockArchiveClient())


def test_fetch_gdelt_articles(pipeline):
    data = pipeline.fetch_gdelt_articles(["ECB"], "2023-01-01", "2023-12-31")
    assert isinstance(data, list)
    assert "title" in data[0]
    # come back to this after implementation


def test_standardize_aritcles(pipeline):
    raw = [{"DocumentIdentifier": "https://example.com/1", "title": "ECB raises rates", "timestamp": "1735689600"}]
    standardized = pipeline.standardize_articles(raw)
    assert isinstance(standardized, list)
    assert isinstance(standardized[0], NewsItem)
    assert standardized[0].title == "ECB raises rates"


def test_fetch_archived_content(pipeline):
    item = NewsItem(source="test", title="ECB raises rates", url="https://example.com")
    enriched = pipeline.fetch_archived_content([item])
    assert enriched[0].raw_metadata.get("archived_text") is not None


def test_load_and_align_with_forex(pipeline, tmp_path): 
        # Create temporary forex file
    forex_data = """
    20100101,1.43880,1.43990,1.43880,1.43880,3
    20100104,1.43020,1.44560,1.42550,1.44120,134321
    """

    f = tmp_path / "forex_sample.txt"
    f.write_text(forex_data)

    # Load forex data
    forex_loader = ForexLoader(str(f), granularity="day")
    df = forex_loader.load()

    # Make sure forex data is loaded properly
    assert not df.empty
    assert "datetime" in df.columns

    # Prepare sample news
    item = NewsItem(source="gdelt", title="ECB raises rates", url="https://example.com", published_at="2010-01-04T00:00:00Z")
    result = pipeline.align_with_forex([item], df)

    # When align_with_forex is not implemented, just skip test
    pytest.skip("align_with_forex not yet implemented")
    