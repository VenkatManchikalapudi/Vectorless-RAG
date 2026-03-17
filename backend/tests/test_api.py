from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_qa_with_search():
    """
    Test the /qa/search endpoint with a mock query and question.
    """
    # Mock data for testing
    query = "Python programming"
    question = "What is Python used for?"

    response = client.post("/qa/search", params={"query": query, "question": question})

    assert response.status_code == 200
    assert isinstance(response.json(), str)
    assert len(response.json()) > 0