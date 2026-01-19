#!/usr/bin/env python3
import sys

cur_sym = None
rows = []

def flush(sym, rows):
    if not sym or not rows:
        return
    # sort by date
    rows.sort(key=lambda x: x[0])

    prev_close = None
    for date, close in rows:
        try:
            c = float(close)
        except:
            continue

        if prev_close is None:
            prev_close = c
            continue

        # simple return
        ret = (c - prev_close) / prev_close if prev_close != 0 else 0.0
        sys.stdout.write(f"{sym},{date},{ret}\n")
        prev_close = c

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    sym, rest = line.split("\t", 1)
    date, close = rest.split(",", 1)

    if cur_sym is None:
        cur_sym = sym

    if sym != cur_sym:
        flush(cur_sym, rows)
        cur_sym = sym
        rows = []

    rows.append((date, close))

flush(cur_sym, rows)
