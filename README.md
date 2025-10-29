# hackernews-api-test

Automated acceptance tests for the Hacker News public API.

## Stack
- Python 3.10+
- `pytest` for the test runner
- `requests` for HTTP
- Optional: `pytest-html` for pretty reports

## Endpoints Under Test
- `GET https://hacker-news.firebaseio.com/v0/topstories.json`
- `GET https://hacker-news.firebaseio.com/v0/item/{id}.json`

## Test Coverage
1. **Retrieve Top Stories**
   - 200 OK, non-empty list, list of ints, basic latency check (<2s)

2. **Retrieve Current Top Story**
   - First ID from Top Stories -> fetch via Items API
   - Validate `type == "story"`, presence of common fields

3. **Retrieve First Comment of Top Story**
   - If `kids` exists, fetch first comment and validate `type == "comment"` and `parent` equals story ID

4. **Edge Cases**
   - Invalid / huge ID returns `null` (maps to Python `None`)
   - Negative IDs handled gracefully

## Getting Started

```bash
# 1) Clone
git clone https://github.com/<your-username>/hackernews-api-test
cd hackernews-api-test

# 2) Create a virtualenv (recommended)
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3) Install dependencies
pip install -r requirements.txt

# 4) Run tests
pytest

# 5) (Optional) Generate an HTML report
pytest --html=report.html --self-contained-html
```

## Project Layout
```
hackernews-api-test/
  ├── src/
  │   └── api_client.py
  ├── tests/
  │   ├── test_comments.py
  │   ├── test_edge_cases.py
  │   ├── test_items_api.py
  │   └── test_top_stories.py
  ├── pytest.ini
  ├── requirements.txt
  └── README.md
```

## CI (Bonus)
A simple GitHub Actions workflow is included to run tests on push/PR. Create a repo named `hackernews-api-test` and push these files.

## Notes
- These tests hit the live public API and may be affected by network variance or changing top stories.
- For a more robust approach, you could add a mock layer for deterministic runs, and JSON schema checks for story/comment structure.
