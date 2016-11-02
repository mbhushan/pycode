#!/usr/bin/python

import sys

def mapper():

    for line in sys.stdin:
        data = line.strip().split("\t")

        if len(data) != 6:
            continue
        date, time, store, item, cost, payment = data
        print ("%s" % (cost))

def main():
    mapper()

if __name__ == '__main__':
    main()

