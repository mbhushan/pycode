#!/usr/bin/python

import sys


def reducer():
    prev = None
    count = 0
    maxCount = 0
    fname = None
    for line in sys.stdin:
        if line != prev and (prev is not None):
            print("%s - %s" % (count, prev))
            if count > maxCount:
                fname = prev
                maxCount = count
            count = 0
        count += 1
        prev = line

    print ("Result: %s - %s" % (maxCount, fname))


def main():
    reducer()

if __name__ == '__main__':
    main()
