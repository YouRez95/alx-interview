#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""

import sys

if __name__ == '__main__':
    filesize = 0
    count = 0
    status = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {num: 0 for num in status}

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            status_code = data[-2]
            if status_code in stats:
                stats[status_code] += 1
            filesize += int(data[-1])
            if count % 10 == 0:
                print("File size: {:d}".format(filesize))
                for i, j in sorted(stats.items()):
                    if j:
                        print("{}: {}".format(i, j))
        print("File size: {:d}".format(filesize))
        for i, j in sorted(stats.items()):
            if j:
                print("{}: {}".format(i, j))
    except KeyboardInterrupt:
        print("File size: {:d}".format(filesize))
        for i, j in sorted(stats.items()):
            if j:
                print("{}: {}".format(i, j))
