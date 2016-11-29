#!/usr/bin/python

import sys

def reducer():
    rmap = {}
    vals = ()
    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            continue
        sum, count = 0, 0
        if data[0] in rmap:
            (sum, count) = rmap[data[0]]
        sum += float(data[1])
        count += 1
        rmap[data[0]] = (sum, count)
    for k,v in rmap.items():
        print(k, v)



def main():
    reducer()


if __name__ == '__main__':
    main()