#!/usr/bin/env python3

import sys

# Iterate through each line from stdin
for line in sys.stdin:
    # Strip whitespace and split the line into word and article_id
    line = line.strip()
    word, article_id = line.split('\t', 1)

    # Emit word-article_id pair
    print(f"{word}\t{article_id}")
