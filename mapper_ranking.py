#!/usr/bin/env python3

import sys

# Initialize inverted index dictionary
inverted_index = {}

# Process input from dataset file
for line in sys.stdin:
    line = line.strip()
    # Assuming each line represents a document with space-separated terms and their TF-IDF scores
    doc, term_tfidf_pairs = line.split(',', 1)
    term_tfidf_pairs = term_tfidf_pairs.split(' ')
    for pair in term_tfidf_pairs:
        term, tfidf = pair.split(':', 1)
        tfidf = float(tfidf)
        # Add term and TF-IDF score to the inverted index
        if term not in inverted_index:
            inverted_index[term] = {}
        inverted_index[term][doc] = tfidf

# Process the inverted index and calculate relevance scores for the query
for term, doc_tfidf in inverted_index.items():
    relevance_score = sum(doc_tfidf.values())
    # Emit key-value pair (relevance_score, term) for sorting in the reducer
    print(f"{relevance_score}\t{term}")
