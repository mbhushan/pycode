#!/usr/bin/python

import sys
from datetime import datetime


def mapper():
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 6:
            continue
        date, time, store, item, cost, payment = data
        weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
        print ("%s\t%s" % (weekday, cost))


def main():
    mapper()

if __name__ == '__main__':
    main()
