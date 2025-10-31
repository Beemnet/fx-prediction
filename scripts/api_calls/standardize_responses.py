import json
import logging
from datetime import datetime, timezone
from typing import Optional, Dict, List, Any
from uuid import uuid4


logger = logging.getLogger(__name__)


class NewsItem:
    def __init__(
            self,
            source : str,
            title: str,
            url: str,
            published_at: Optional[str] = None,
            snippet: Optional[str] = None,
            publisher: Optional[str] = None,
            language: Optional[str] = None,
            country: Optional[str] = None,
            topics: Optional[List[str]] = None,
            raw_metadata: Optional[Dict[str, Any]] = None,
        ):
        
        self.id = f"{source}_{uuid4().hex[:8]}"
        self.source = source
        self.title = title or ""
        self.url = url or ""
        self.snippet = snippet or ""
        self.publisher = publisher or ""
        self.language = language or "en"
        self.country = country
        self.topics = topics or []
        self.raw_metadata = raw_metadata or {}
        self.published_at = self._normalize_datetime(published_at)
        
        
    def _normalize_datetime(self, ts: Optional[str]) -> Optional[str]:
        if ts is None:
            return None
        try:
            s = str(ts).strip()
            # numeric epoch (seconds or milliseconds)
            if s.isdigit():
                val = int(s)
                # Heuristic: > 1e12 → ms, otherwise seconds
                if val > 10**12:
                    val = val // 1000
                dt = datetime.fromtimestamp(val, tz=timezone.utc)
                return dt.isoformat()
            # Try ISO parse (Z -> +00:00)
            try:
                dt = datetime.fromisoformat(s.replace("Z", "+00:00"))
                if dt.tzinfo is None:
                    dt = dt.replace(tzinfo=timezone.utc)
                return dt.isoformat()
            except Exception:
                # final fallback: return raw string
                logger.warning("Could not parse datetime %r", ts)
                return s
        except Exception as e:
            logger.warning("Date normalization error for %r: %s", ts, e)
            return str(ts)        

    @classmethod
    def from_gdelt(cls, raw: Dict[str, Any]) -> "NewsItem":
        # Common GDELT fields: 'DocumentIdentifier' (url), 'V2Themes', 'V2Persons', 'V2Locations', 'DATE'
        title = raw.get("title") or raw.get("Title") or raw.get("GLOBALEventID") or ""
        # identifier could include id or url
        url = raw.get("DocumentIdentifier") or raw.get("url") or raw.get("newsUrl") or raw.get("link") or ""
        
        # GDELT date may be like YYYYMMDD in 'DATE' field, or 'date' or 'timestamp'
        published_at = raw.get("DATE") or raw.get("date") or raw.get("timestamp") or raw.get("published_datetime_utc") or None
        snippet = raw.get("snippet") or raw.get("Summary") or ""
        publisher = raw.get("source") or raw.get("SourceCommonName") or raw.get("source_name") or ""


        return cls(
            source="gdelt",
            title=title,
            url=url,
            published_at=published_at,
            snippet=snippet,
            publisher=publisher,
            raw_metadata={"original_response": raw},
        )
    

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "source": self.source,
            "title": self.title,
            "url": self.url,
            "snippet": self.snippet,
            "publisher": self.publisher,
            "language": self.language,
            "country": self.country,
            "topics": self.topics,
            "published_at": self.published_at,
            "raw_metadata": self.raw_metadata,
        }

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False, indent=2)