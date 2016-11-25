#!/usr/bin/python

import sys
import shlex


def mapper():
    for line in sys.stdin:
        # data = shlex.split(line)
        data = line.strip().split(" ")
        if len(data) != 10:
            continue
        #access = shlex.split(data[5])
        #access = data[6].split(" ")
        #if len(access) != 3:
        #    continue
        #print("ACCESS: %s" % (access))
        #path = access[1]
        path = data[6]
        if path.startswith("http://www.the-associates.co.uk"):
            path = path[31:]
        print("%s" %(path))



def main():
    mapper()

if __name__ == '__main__':
    main()