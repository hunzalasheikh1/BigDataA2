#!/usr/bin/env python3

import sys

current_word = None
current_article_ids = []

# Iterate through each line from stdin
for line in sys.stdin:
    # Strip whitespace and split the line into word and article_ids
    line = line.strip()
    word, article_ids = line.split('\t', 1)

    # Split the article_ids into a list
    article_ids = article_ids.split(',')

    # If the word is the same as the previous word, append article_ids to the list
    if current_word == word:
        current_article_ids.extend(article_ids)
    else:
        # If the word is different, emit the previous word and its article_ids
        if current_word:
            print(f"{current_word}\t{','.join(map(str, current_article_ids))}")
        # Reset variables for the new word
        current_word = word
        current_article_ids = article_ids

# Emit the last word and its article_ids
if current_word:
    print(f"{current_word}\t{','.join(map(str, current_article_ids))}")
