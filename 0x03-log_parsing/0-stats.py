#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics:
- Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
  <status code> <file size>
- After every 10 lines and/or a keyboard interruption (CTRL + C),
  print statistics
"""
import sys
import re


def print_stats(total_size, status_codes):
    """
    Print the statistics:
    - Total file size
    - Number of lines by status code in ascending order
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """
    Main function to process the logs
    """
    # Regular expression for validating log format
    pattern = r'^\d+\.\d+\.\d+\.\d+ - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
    
    # Alternatively, a more general pattern that matches the example outputs
    alt_pattern = r'^[\d\.]+ - \[[^\]]*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
    
    # Using the more general pattern since the date format varies in the examples
    pattern = alt_pattern
    
    # Initialize variables
    total_size = 0
    line_count = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
    
    try:
        for line in sys.stdin:
            line = line.strip()
            match = re.match(pattern, line)
            
            if match:
                status_code = int(match.group(1))
                file_size = int(match.group(2))
                
                # Update total file size
                total_size += file_size
                
                # Update status code count if it's one we're tracking
                if status_code in status_codes:
                    status_codes[status_code] += 1
                
                # Increment line count
                line_count += 1
                
                # Print statistics every 10 lines
                if line_count % 10 == 0:
                    print_stats(total_size, status_codes)
    
    except KeyboardInterrupt:
        # Handle keyboard interruption (CTRL + C)
        pass
    
    finally:
        # Print final statistics
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()