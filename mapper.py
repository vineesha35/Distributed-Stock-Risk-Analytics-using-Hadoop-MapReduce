#!/usr/bin/env python3
import sys

# Loop through input from HDFS
for line in sys.stdin:
    line = line.strip()


    # CHECK: common header text (e.g. Ticker, Date, or date)
    if 'Ticker' in line or 'Date' in line or 'date' in line:
        continue

    try:
        # Split by comma
        data = line.split(',')

        # Ensure the line has enough columns (This is 6)
        if len(data) < 6:
            continue

        # CHECK: Ticker is in the first column (index 0)
        ticker = data[0].strip()

        
        # Convert Closing Price to a float (closing Price is in the 6th column (index 5))
        closing_price = float(data[5].strip())

        # Output the intermediate key value pair (Key=Ticker and Value=Closing Price)
        print(f"{ticker}\t{closing_price}")

    except ValueError:
        # Catches lines where closing price (index 5) is not a valid number 
        continue
    except IndexError:
        # Catches lines that are too short 
        continue
    except Exception:
        # Catch any other unexpected error and skip the line
        continue
