#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
import csv

def reducer():
    """
    The goal is to have the output from the reducer with the following fields for each forum post:
    "id"  "title"  "tagnames"  "author_id"  "node_type"  "parent_id"  "abs_parent_id"  "added_at"
    "score"  "reputation"  "gold"  "silver"  "bronze"
    """
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
    count = 0
    output = []
    for line in reader:
        count += 1
        if count % 2 == 0:
            output.extend(line[2:5])
            output.append(line[0])
            output.extend(line[5:])
            output.extend(prev[2:])
            writer.writerow(output)
            del output[:]
            continue
        prev = line


def main():
    reducer()


if __name__ == '__main__':
    main()
