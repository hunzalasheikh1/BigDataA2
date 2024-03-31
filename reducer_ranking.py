#!/usr/bin/env python3

import sys

current_relevance_score = None
current_term = None
term_count = 0

# Process input from the mapper
for line in sys.stdin:
    line = line.strip()
    relevance_score, term = line.split('\t', 1)
    relevance_score = float(relevance_score)
    
    # If the relevance score changes, output the term with the highest relevance score
    if current_relevance_score != relevance_score:
        if current_relevance_score is not None:
            print(f"{current_relevance_score}\t{current_term}\t{term_count}")
        current_relevance_score = relevance_score
        current_term = term
        term_count = 1
    else:
        term_count += 1

# Output the last term and relevance score
if current_relevance_score is not None:
    print(f"{current_relevance_score}\t{current_term}\t{term_count}")
