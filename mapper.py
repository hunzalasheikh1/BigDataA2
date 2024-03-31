#!/usr/bin/env python3

import sys
import csv
import string

# Function to remove punctuation and convert text to lowercase
def clean_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# Read input from stdin
for line in sys.stdin:
    # Strip whitespace and split the line into fields
    line = line.strip()
    fields = line.split(',')

    # Check if the line has the expected number of fields
    if len(fields) == 4:
        article_id = fields[0]
        section_text = fields[3]

        # Clean the section text
        section_text = clean_text(section_text)

        # Tokenize the section text into words
        words = section_text.split()

        # Emit word-article_id pairs
        for word in words:
            print(f"{word}\t{article_id}")
