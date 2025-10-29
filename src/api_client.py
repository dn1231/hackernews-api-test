import requests
from typing import Any, List, Optional

BASE_URL = "https://hacker-news.firebaseio.com/v0"

class HNClient:
    def __init__(self, base_url: str = BASE_URL, timeout: float = 10.0):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout

    def _get(self, path: str) -> requests.Response:
        url = f"{self.base_url}/{path.lstrip('/')}"
        resp = requests.get(url, timeout=self.timeout)
        resp.raise_for_status()
        return resp

    def get_top_stories_ids(self) -> List[int]:
        """Return list of story IDs (ints)."""
        resp = self._get("topstories.json")
        data = resp.json()
        if not isinstance(data, list):
            raise AssertionError("Expected list for topstories.json")
        # HN sometimes returns large ints; ensure ints
        return [int(x) for x in data]

    def get_item(self, item_id: int) -> Optional[dict]:
        """Return item JSON or None (HN returns null for missing)."""
        resp = self._get(f"item/{int(item_id)}.json")
        data = resp.json()
        return data  # may be None
