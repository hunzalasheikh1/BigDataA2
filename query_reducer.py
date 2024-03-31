#!/usr/bin/env python3

import sys

current_doc_id = None
total_score = 0

# Process each input line from the mapper
for line in sys.stdin:
    # Strip whitespace and split the line into document ID and score
    doc_id, score = line.strip().split('\t', 1)

    # Convert score to int
    score = int(score)

    # If the document ID is the same as the previous one, accumulate the scores
    if current_doc_id == doc_id:
        total_score += score
    else:
        # If the document ID is different, emit the previous document ID and total score
        if current_doc_id:
            print(f"{current_doc_id}\t{total_score}")
        # Reset variables for the new document ID
        current_doc_id = doc_id
        total_score = score

# Emit the last document ID and total score
if current_doc_id:
    print(f"{current_doc_id}\t{total_score}")
