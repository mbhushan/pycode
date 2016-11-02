#!/usr/bin/python

import sys


def reducer():
    total_sale = 0
    total_count = 0
    for line in sys.stdin:
        cost = line.strip()
        try:
            cost = float(cost)
            total_sale += cost
            total_count += 1
        except ValueError:
            continue
    print ("%s" % (total_count))
    print ("%s" % (total_sale))


def main():
    reducer()


if __name__ == '__main__':
    main()