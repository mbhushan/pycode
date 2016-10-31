#!/usr/bin/python

import sys


def reducer():
    maxsale = 0
    prevstore = None

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue
        thisstore, thissale = data
        if prevstore and prevstore != thisstore:
            print("{0}\t{1}".format(prevstore, maxsale))
            maxsale = 0

        prevstore = thisstore
        maxsale = max(maxsale, float(thissale))
    if prevstore is not None:
        print("{0}\t{1}".format(prevstore, maxsale))


def main():
    reducer()

if __name__ == '__main__':
    main()