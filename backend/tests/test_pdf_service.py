from app.services.pdf_service import extract_text_from_pdf, index_pdf_text, search_pdf_content

def test_page_level_indexing():
    """
    Test page-level indexing and retrieval functionality.
    """
    # Mock data: document with page-level content
    documents = {
        "doc1": {
            1: "This is the first page about Python programming.",
            2: "This is the second page about AI and machine learning."
        },
        "doc2": {
            1: "This page discusses keyword search and retrieval."
        }
    }

    # Index the documents
    index_pdf_text(documents)

    # Perform a search
    results = search_pdf_content("Python")

    # Validate results
    assert ("doc1", 1) in results
    assert ("doc1", 2) not in results
    assert ("doc2", 1) not in results