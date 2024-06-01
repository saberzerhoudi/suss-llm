from rank_bm25 import BM25Okapi
from typing import List

class BM25Baseline:
    def __init__(self, corpus: List[List[str]]):
        """
        Initializes the BM25 model with a given corpus.
        :param corpus: A list of documents, where each document is represented as a list of words.
        """
        self.tokenized_corpus = corpus
        self.model = BM25Okapi(self.tokenized_corpus)

    def search(self, query: str) -> List[float]:
        """
        Searches the corpus using the given query.
        :param query: The search query as a string.
        :return: A list of scores for each document in the corpus.
        """
        query_tokens = query.split()
        scores = self.model.get_scores(query_tokens)
        return scores

    def get_top_n(self, query: str, n=10) -> List[int]:
        """
        Retrieves the top N documents for a given query.
        :param query: The search query as a string.
        :param n: The number of top documents to retrieve.
        :return: A list of indices for the top N documents.
        """
        query_tokens = query.split()
        top_n = self.model.get_top_n(query_tokens, n=n)
        return top_n
    
    
    
def main():
    # Example corpus and query
    corpus = [
        "hello world".split(),
        "world of tanks".split(),
        "machine learning in python".split()
    ]
    query = "python world"

    # Initialize and use the BM25 model
    bm25 = BM25Baseline(corpus)
    scores = bm25.search(query)
    print("Document scores:", scores)

    top_docs = bm25.get_top_n(query, n=2)
    print("Top 2 documents:", top_docs)

if __name__ == "__main__":
    main()