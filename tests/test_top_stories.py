import time
from src.api_client import HNClient

client = HNClient()

def test_top_stories_returns_non_empty_list_and_ints():
    ids = client.get_top_stories_ids()
    assert isinstance(ids, list) and len(ids) > 0, "Top stories should be a non-empty list"
    assert all(isinstance(i, int) for i in ids), "All IDs should be integers"

def test_top_stories_performance_under_2s():
    start = time.time()
    _ = client.get_top_stories_ids()
    elapsed = time.time() - start
    assert elapsed < 2.0, f"Top stories call should be fast (<2s), was {elapsed:.3f}s"
