#!/usr/bin/python

import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    word_map = {}
    rlist = []
    for line in reader:
        if len(line) < 5:
            continue
        body = line[4]
        words = re.split(r'[;:,-<>!?#=.()/#"\[\]/\t/\n\s]\s*', body)
        for key in words:
            if key.lower() == 'fantastically':
                if key.lower() in word_map:
                    rlist = word_map[key.lower()]
                rlist.append(int(line[0]))
                word_map[key.lower()] = rlist

    #writer.writerow(line)
    rlist.sort()
    print ("%s" % (rlist))


def main():
    mapper()

if __name__ == '__main__':
    main()