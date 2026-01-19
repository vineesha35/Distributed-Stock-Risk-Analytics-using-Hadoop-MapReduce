#!/usr/bin/env python3
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
    print(f"{ticker}\t{date},{openp},{high},{low},{close},{volume}")
