import json
from datetime import datetime, timezone
from typing import Optional, Dict, Any, List
import logging
from uuid import uuid4

class NewsItem:
    '''
    standardized news article item, has json serializable list of news sources from multiple apis via rapidapi
    '''

    def __init__(
            self,
            source: str,
            title:str,
            url:str,
            published_at: Optional[str]=None,
            snippet : Optional[str] = None,
            publisher: Optional[str]=None,
            language:Optional[str]=None,
            country:Optional[str]=None,
            topics:Optional[str]=None,
            raw_metadata:Optional[Dict[str, Any]]=None
            ):
        
        self.id = f"{source}_{uuid4().hex[:8]}"
        self.source = source
        self.title = title
        self.url = url
        self.snippet = snippet or ""
        self.publisher = publisher or ""
        self.language = language or "en"
        self.country = country
        self.topics = topics or []
        self.raw_metadata = raw_metadata or {}
        
        self.published_at = self._normalize_datetime(published_at)
    


    # Helpers
    def _normalize_datetime(self, ts: Optional[str]) -> Optional[str]:
        # convert to iso format, utc

        if not ts:
            return None
        try: 
            ts = int(ts)
            if ts > 10**12: # in milliseconds
                ts //= 1000 # to seconds
            dt = datetime.fromtimestamp(ts, tz=timezone.utc)
            return dt.isoformat()
            
        except Exception:
            logging.warning(f"Date parsing failed, saving date as {date_str}")
            return str(ts) # parsing fail
        

    # factory constructors 

    @classmethod
    def from_google_v13(cls, response: Dict[str, Any]) -> "NewsItem":
        items = response.get("items", [])
        news_list = []
        for item in items:
            news_list.append(
                cls(
                    source="google_news_v13",
                    title=item.get("title", ""),
                    snippet=item.get('snippet', ''),
                    url=item.get('url', ''),
                    publisher = item.get('publisher', ''),
                    published_at=str(item.get("timestamp")),
                    # TODO: redefine this, storage recklessness to keep it
                    raw_metadata={
                        "api_version": 13,
                        "original_response": item
                    }

                )
            )

            #if subnews
            for sub in item.get("subnews", []):
                news_list.append(
                    cls(
                        source="google_news_v13_sub",
                        title=sub.get("title", ""),
                        snippet=sub.get("snippet", ""),
                        url=sub.get("newsUrl", ""),
                        publisher=sub.get("publisher", ""),
                        published_at=sub.get("timestamp"),
                        raw_metadata={
                            "api_version": 13,
                            "parent_title": item.get("title"),
                            "original_response": sub,
                        },
                    )
                )
            return news_list
    

    # serialization 

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id" : self.id,
            "source" : self.source,
            "title" : self.title,
            "url" : self.url,
            "snippet" : self.snippet,
            "publisher" : self.publisher,
            "language" : self.language,
            "country" : self.country, 
            "topics" : self.topics,
            "published_at" : self.published_at,
            "raw_metadata" : self.raw_metadata
        }
    
    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=4)
    

from pathlib import Path

SAMPLES_DIR = Path(__file__).parent / "../../tests/samples"

def run_sample(filename):
    path = SAMPLES_DIR / filename
    with open(path, "r", encoding='utf-8') as f:
        data = json.load(f)
        
    news_items = NewsItem.from_google_v13(data)
    print(f"Parsed {len(news_items)} total items")
    print(news_items[0].to_json())

    # Save all to JSON file
    with open(f"{SAMPLES_DIR}/parsed_{filename}", "w") as f:
        json.dump([n.to_dict() for n in news_items], f, indent=2)

run_sample("google_news_v13_sample.json")