#!/usr/bin/env python3
import sys

# Reducer just passes through in a clean consistent format
for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    ticker, rest = line.split("\t", 1)
    print(f"{ticker},{rest}")
