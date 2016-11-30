#!/usr/bin/python
"""
Your mapper function should print out 10 lines containing longest posts, sorted in
ascending order from shortest to longest.
Please do not use global variables and do not change the "main" function.
"""
import sys
import csv
import heapq


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    heap = []
    for line in reader:
        # YOUR CODE HERE
        post = line
        if len(heap) < 10:
            heapq.heappush(heap, post)
        else:
            top = heapq.heappop(heap)
            key = top if sum([len(i) for i in top]) > sum([len(i) for i in post]) else post
            heapq.heappush(heap, key)
    heap = sorted(heap, key = lambda x: sum([len(i) for i in x]) )
    for key in heap:
        print("%s" % (key))

        #writer.writerow(line)


test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"333\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"88888888\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"11111111111\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"1000000000\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"22\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"4444\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"666666\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"55555\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"999999999\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"7777777\"\t\"\"
"""


# This function allows you to test the mapper with the provided test string
def main():
    from io import StringIO
    sys.stdin = StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__


main()
