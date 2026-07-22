#!/usr/bin/python3
"""Script that reads stdin and computes size and status-code metrics."""
import sys


def print_stats(total_size, codes):
    """Print the accumulated file size and status-code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(codes):
        if codes[code] > 0:
            print("{}: {}".format(code, codes[code]))


if __name__ == "__main__":
    total_size = 0
    codes = {200: 0, 301: 0, 400: 0, 401: 0,
             403: 0, 404: 0, 405: 0, 500: 0}
    count = 0
    try:
        for line in sys.stdin:
            parts = line.split()
            if len(parts) >= 2:
                try:
                    total_size += int(parts[-1])
                except ValueError:
                    pass
                try:
                    code = int(parts[-2])
                    if code in codes:
                        codes[code] += 1
                except ValueError:
                    pass
            count += 1
            if count % 10 == 0:
                print_stats(total_size, codes)
    except KeyboardInterrupt:
        print_stats(total_size, codes)
        raise
    print_stats(total_size, codes)
