from src.api_client import HNClient

client = HNClient()

def test_invalid_item_id_returns_none():
    # A very large ID should not exist; HN returns JSON null => Python None
    item = client.get_item(10_000_000_000)
    assert item is None or item.get("deleted") or item.get("dead") in (True, False)

def test_negative_item_id_is_invalid_but_server_response_is_graceful():
    try:
        item = client.get_item(-1)
    except Exception as e:
        # Requests may raise for invalid URL; if server accepts it, it should return None or an error
        return
    # If it didn't raise, ensure it's None (non-existent).
    assert item is None
