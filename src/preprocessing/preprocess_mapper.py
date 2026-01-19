#!/usr/bin/env python3

import os

def get_ticker():
    # works in streaming; try multiple keys because Windows/local mode can vary
    path = (os.environ.get("mapreduce_map_input_file")
            or os.environ.get("map_input_file")
            or "")
    base = os.path.basename(path)           # e.g., "aaba.us.txt"
    name = base.split(".")[0]               # "aaba"
    return name.upper() if name else "UNKNOWN"




import os
import sys

# Hadoop provides this during streaming jobs
filename = os.environ.get("map_input_file", "")

# Local fallback: you can pass a ticker via env var
ticker = os.environ.get("TICKER", "")

if not ticker:
    if filename:
        base = os.path.basename(filename)
        ticker = base.split(".")[0].upper()
    else:
        ticker = "UNKNOWN"

for line in sys.stdin:
    line = line.strip()
    if not line or line.startswith("Date"):
        continue

    parts = line.split(",")
    if len(parts) < 6:
        continue

    date, openp, high, low, close, volume = parts[:6]
    ticker = get_ticker()
    print(f"{ticker},{date},{openp},{high},{low},{close},{volume}")
