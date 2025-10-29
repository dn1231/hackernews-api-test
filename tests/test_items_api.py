from src.api_client import HNClient

client = HNClient()

def test_current_top_story_details_type_story_and_fields():
    ids = client.get_top_stories_ids()
    top_id = ids[0]
    item = client.get_item(top_id)
    assert item is not None, "Top story item should exist"
    assert item.get("id") == top_id, "Item id should match the requested id"
    assert item.get("type") == "story", f"Expected type 'story' but got {item.get('type')}"
    # Common required fields for a story; url may be absent on 'Ask HN'
    required_fields = ["id", "by", "time", "title", "type"]
    for f in required_fields:
        assert f in item, f"Missing required field: {f}"
