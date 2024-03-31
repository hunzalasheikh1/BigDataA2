#!/usr/bin/env python3

import sys

current_word = None
current_article_ids = []

# Iterate through each line from stdin
for line in sys.stdin:
    # Strip whitespace and split the line into word and article_id
    line = line.strip()
    word, article_id = line.split('\t', 1)

    # Convert article_id to int
    try:
        article_id = int(article_id)
    except ValueError:
        # Ignore lines where article_id is not an integer
        continue

    # If the word is the same as the previous word, add the article_id to the list
    if current_word == word:
        current_article_ids.append(article_id)
    else:
        # If the word is different, emit the previous word and its article_ids
        if current_word:
            print(f"{current_word}\t{','.join(map(str, current_article_ids))}")
        # Reset variables for the new word
        current_word = word
        current_article_ids = [article_id]

# Emit the last word and its article_ids
if current_word:
    print(f"{current_word}\t{','.join(map(str, current_article_ids))}")
