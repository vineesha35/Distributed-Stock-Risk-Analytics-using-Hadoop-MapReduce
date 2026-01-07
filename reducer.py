#!/usr/bin/env python3
import sys

# Variables for aggregation
current_ticker = None
total_price = 0.0
total_count = 0

# Loop through lines from the mapper.py 
for line in sys.stdin:
    try:
        # Split the line into Key (Ticker) and Value (Price) and separate by TAB ('\t')
        line = line.strip()
        key, price_str = line.split('\t', 1)
        
        # Convert to numeric types
        price = float(price_str)
        count = 1 
        
    except ValueError:
        # Skip lines that ccannot be parsed into the expected numeric formats
        continue
    except Exception:
        continue # Skip any additional parsing errors

    # MapReduce Grouping Logic (AKA Reducer Core)
    # Aggregate if on same ticker
    if current_ticker == key:
        
        total_price += price
        total_count += count
    else:
        # Output previous result if new ticker,  the result of the previous one
        if current_ticker:
            # Calculate final average
            final_average = total_price / total_count if total_count else 0.0
            
            # Output the final result (i.e.,Ticker, Total Price, Total Count, Final Average)
            print(f"{current_ticker}\t{total_price}\t{total_count}\t{final_average}")

        # Reset counters for the new ticker
        current_ticker = key
        total_price = price
        total_count = count

# Output last key-value pair after the loop finished
if current_ticker:
    final_average = total_price / total_count if total_count else 0.0
    print(f"{current_ticker}\t{total_price}\t{total_count}\t{final_average}")
