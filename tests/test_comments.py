import pytest
from src.api_client import HNClient

client = HNClient()

def test_first_comment_of_top_story_if_exists():
    ids = client.get_top_stories_ids()
    top_id = ids[0]
    story = client.get_item(top_id)
    assert story is not None and story.get("type") == "story"

    kids = story.get("kids")
    if not kids:
        pytest.skip("Top story has no comments (kids) to validate")

    first_comment_id = kids[0]
    comment = client.get_item(first_comment_id)
    assert comment is not None, "Comment item should exist"
    assert comment.get("type") == "comment", f"Expected a comment, got {comment.get('type')}"
    assert comment.get("parent") == top_id, "Comment parent should reference the story id"
