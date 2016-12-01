#!/usr/bin/python

import sys
import csv
import re

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    word_map = {}
    count = 0
    for line in reader:
        if len(line) < 5:
            continue
        body = line[4]
        words = re.split(r'[;:,-<>!?#=.()/#"\[\]/\t/\n\s]\s*', body)
        for key in words:
            if key.lower() == 'fantastic':
                count += 1

    #writer.writerow(line)
    print ("%s" % (count))


def main():
    mapper()

if __name__ == '__main__':
    main()