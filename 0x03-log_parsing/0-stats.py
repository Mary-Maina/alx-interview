#!/usr/bin/python3
"""
Log parsing
"""

import sys
import re
import signal

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)  # Handle Ctrl+C

total_size = 0
status_codes = {}
line_count = 0

def print_stats():
    global total_size, status_codes

    print("Total file size: File size:", total_size)

    sorted_status_codes = sorted(status_codes.items())  # Sort by status code
    for code, count in sorted_status_codes:
        print(f"{code}: {count}")

def process_line(line):
    global total_size, status_codes

    match = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[[^\]]+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)', line)
    if match:
        try:
            status_code = int(match.group(2))
            file_size = int(match.group(3))

            total_size += file_size

            if status_code in [200, 301, 400, 401, 403, 404, 405, 500]:
                status_codes[status_code] = status_codes.get(status_code, 0) + 1

        except ValueError:
            pass # Ignore lines with bad status codes or file sizes

for line in sys.stdin:
    process_line(line.strip())  # Remove leading/trailing whitespace
    line_count += 1

    if line_count % 10 == 0:
        print_stats()

print_stats() # Print stats after processing all lines
