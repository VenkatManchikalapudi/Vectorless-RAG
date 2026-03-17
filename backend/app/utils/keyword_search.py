import os
from collections import defaultdict
from typing import List, Dict

class KeywordSearch:
    def __init__(self):
        self.index = defaultdict(list)

    def build_index(self, documents: Dict[str, Dict[int, str]]):
        """
        Build an inverted index from a dictionary of documents with page-level granularity.
        :param documents: A dictionary where keys are document IDs and values are dictionaries mapping page numbers to content.
        """
        for doc_id, pages in documents.items():
            for page_number, content in pages.items():
                words = content.split()
                for word in words:
                    normalized_word = word.lower()
                    self.index[normalized_word].append((doc_id, page_number))

    def search(self, query: str) -> List[Dict[str, int]]:
        """
        Perform a keyword-based search with page-level results.
        :param query: The search query string.
        :return: A list of tuples containing document IDs and page numbers matching the query.
        """
        query_words = query.lower().split()
        results = set()
        for word in query_words:
            if word in self.index:
                results.update(self.index[word])
        return list(results)

# Example usage
if __name__ == "__main__":
    documents = {
        "doc1": {
            1: "This is a sample document about AI and machine learning.",
            2: "Another document discussing Python and programming."
        },
        "doc2": {
            1: "This document is about keyword search and retrieval."
        }
    }

    search_engine = KeywordSearch()
    search_engine.build_index(documents)

    query = "Python AI"
    print("Search results for query:", query)
    print(search_engine.search(query))