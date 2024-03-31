#!/usr/bin/env python3

import sys
import json

index = {}

for line in sys.stdin:
    doc_id, text = line.strip().split('\t', 1)
    words = text.split()
    for word in words:
        index.setdefault(word, set()).add(doc_id)

# Emit the index
for word, postings in index.items():
    print(f"{word}\t{json.dumps(list(postings))}")
