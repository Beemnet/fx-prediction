## all functions are callable, but not yet implemented

from typing import List, Dict, Any
from scripts.api_calls.standardize_responses import NewsItem ## copy this code from branch tdd sth

class NewsPipeline: 

    def __init__(self, gdelt_client, archive_client, forex_client=None):
        self.gdelt_client = gdelt_client
        self.archive_client = archive_client
        self.forex_client = forex_client


    def fetch_gdelt_articles(self, keywords: List[str], start_date: str, end_date: str) -> List[Dict[str, Any]]:
        return self.gdelt_client.query(keywords, start_date, end_date)
    
    def standardize_articles(self, raw_articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        return [NewsItem.from_gdelt(a) for a in raw_articles]
    
    def fetch_archived_content(self, news_items: List[NewsItem]) -> List[NewsItem]:
        enriched = []
        for item in news_items:
            text = self.archive_client.fetch_text(item.url)
            item.raw_metadata["archived_text"] = text
            enriched.append(item)

        return enriched
    
    def align_with_forex(self, news_items: List[NewsItem], forex_data: Any):
        raise NotImplementedError("align with forex not implemented.")

