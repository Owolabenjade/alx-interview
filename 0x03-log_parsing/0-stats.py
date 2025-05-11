#!/usr/bin/python3
"""
Script that reads stdin line by line and computes metrics.
"""
import sys
import re


def print_stats(total_size, status_codes):
    """Print accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """Main function to process the logs."""
    total_size = 0
    line_count = 0
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    # Regular expression to validate and extract data from log lines
    pattern = r'^\S+ - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'

    try:
        for line in sys.stdin:
            try:
                match = re.match(pattern, line.strip())
                if match:
                    status_code = int(match.group(1))
                    file_size = int(match.group(2))

                    # Update total file size
                    total_size += file_size

                    # Update status code count if it's in our dictionary
                    if status_code in status_codes:
                        status_codes[status_code] += 1

                    # Increment line count
                    line_count += 1

                    # Print stats every 10 lines
                    if line_count % 10 == 0:
                        print_stats(total_size, status_codes)
            except Exception:
                # Skip lines that cause errors during processing
                pass

    except KeyboardInterrupt:
        # Handle CTRL+C interruption
        pass

    finally:
        # Print final stats
        print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
