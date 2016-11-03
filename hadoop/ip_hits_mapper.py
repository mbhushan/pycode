#!/usr/bin/python

import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split(" ")
        #print(data[0])
        if len(data) != 10:
            continue
        #print(data)
        if data[0].strip() == "10.99.99.186":
            print("%s" % (data[0]))



def main():
    mapper()

if __name__ == '__main__':
    main()