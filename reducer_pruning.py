#!/usr/bin/env python3

import sys
import json

THRESHOLD = 100

for line in sys.stdin:
    term, postings = line.strip().split('\t', 1)
    postings = json.loads(postings)
    
    # Prune terms with low frequency
    if len(postings) >= THRESHOLD:
        print(f"{term}\t{json.dumps(postings)}")
