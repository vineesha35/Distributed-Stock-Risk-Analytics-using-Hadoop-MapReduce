#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    parts = line.split(",")
    if len(parts) < 7:
        continue

    sym, date, open_p, high, low, close, vol = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6]

    # key = symbol, value = date + close
    # we'll compute returns in reducer using sorted dates
    sys.stdout.write(f"{sym}\t{date},{close}\n")
