#!/usr/bin/env python3

import sys

# Load the inverted index into memory
inverted_index = {}

# Read the inverted index from file
with open('inverted_index.txt', 'r') as index_file:
    for line in index_file:
        word, postings = line.strip().split('\t')
        inverted_index[word] = postings.split(',')

# Process each query from stdin
for line in sys.stdin:
    # Strip whitespace and split the line into query terms
    query_terms = line.strip().split()

    # Initialize a dictionary to store document scores
    document_scores = {}

    # For each query term, calculate document scores
    for term in query_terms:
        # If the term exists in the inverted index, retrieve its postings list
        if term in inverted_index:
            postings_list = inverted_index[term]
            # Increment document scores for each document in the postings list
            for doc_id in postings_list:
                document_scores[doc_id] = document_scores.get(doc_id, 0) + 1

    # Emit document scores for each query term
    for doc_id, score in document_scores.items():
        print(f"{doc_id}\t{score}")
