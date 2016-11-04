#!/usr/bin/python

import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split(" ")
        #print(data)
        if len(data) != 10:
            continue
        #print(data)
        if data[6].strip() == "/assets/js/the-associates.js":
            print("%s" % (data[6]))



def main():
    mapper()

if __name__ == '__main__':
    main()