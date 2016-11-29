#!/usr/bin/python
"""
Your mapper function should print out 10 lines containing longest posts, sorted in
ascending order from shortest to longest.
Please do not use global variables and do not change the "main" function.
"""
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


test_text = """\"\"\t\"\"\t\"\"\t\"\"\t\"This is one sentence\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Also fantastic one sentence!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Hey!\nTwo fantastic sentences!\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"One. Two! Three?\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"One Period. Two fantastic Sentences\"\t\"\"
\"\"\t\"\"\t\"\"\t\"\"\t\"Three\nlines, one fantastics sentence\n\"\t\"\"
"""


# This function allows you to test the mapper with the provided test string
def main():
    from io import StringIO
    sys.stdin = StringIO(test_text)
    mapper()
    sys.stdin = sys.__stdin__


main()
