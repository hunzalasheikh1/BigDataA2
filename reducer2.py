#!/usr/bin/env python3

import sys

current_word = None
article_ids = []

# Iterate through each line from stdin
for line in sys.stdin:
    # Strip whitespace and split the line into word and article_id
    line = line.strip()
    word, article_id = line.split('\t', 1)

    # If the word is the same as the previous word, add the article_id to the list
    if current_word == word:
        article_ids.append(article_id)
    else:
        # If the word is different, emit the previous word and its article_ids
        if current_word:
            print(f"{current_word}\t{','.join(article_ids)}")
        # Reset variables for the new word
        current_word = word
        article_ids = [article_id]

# Emit the last word and its article_ids
if current_word:
    print(f"{current_word}\t{','.join(article_ids)}")
