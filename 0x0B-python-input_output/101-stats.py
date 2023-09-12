#!/usr/bin/python3
import sys

def print_metrics(total_size, status_codes):
    print(f"File size: {total_size}")
    for status_code in sorted(status_codes.keys()):
        print(f"{status_code}: {status_codes[status_code]}")

def parse_line(line):
    parts = line.split()
    return int(parts[-1]), parts[-2]

total_size = 0
status_codes = {}

try:
    for i, line in enumerate(sys.stdin, start=1):
        file_size, status_code = parse_line(line)
        total_size += file_size
        status_codes[status_code] = status_codes.get(status_code, 0) + 1
        
        if i % 10 == 0:
            print_metrics(total_size, status_codes)

except KeyboardInterrupt:
    print_metrics(total_size, status_codes)
