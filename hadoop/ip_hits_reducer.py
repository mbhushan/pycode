#!/usr/bin/python

import sys


def reducer():
    hits = 0
    for line in sys.stdin:
        hits += 1
    print (hits)


def main():
    reducer()


if __name__ == '__main__':
    main()