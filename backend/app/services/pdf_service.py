# PDF text extraction and summarization utilities
import PyPDF2
import os
from backend.app.utils.keyword_search import KeywordSearch

# Initialize the keyword search engine
search_engine = KeywordSearch()

def extract_text_from_pdf(filepath):
    """Extract text from each page of a PDF file using PyPDF2."""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"PDF file not found: {filepath}")

    page_text = {}
    with open(filepath, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page_number, page in enumerate(reader.pages, start=1):
            page_text[page_number] = page.extract_text() or ""

    return page_text

def index_pdf_text(documents):
    """
    Index the text content of multiple documents with page-level granularity.
    :param documents: A dictionary where keys are document IDs and values are dictionaries mapping page numbers to content.
    """
    search_engine.build_index(documents)

def search_pdf_content(query):
    """
    Search indexed PDF content using a keyword-based query.
    :param query: The search query string.
    :return: A list of document IDs matching the query.
    """
    return search_engine.search(query)

