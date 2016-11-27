#!/usr/bin/python
"""
Your goal for this task is to write mapper and reducer code
that will combine some of the forum and user data.
In relational algebra, this is known as a join operation.
At the moment, this is not an auto-gradable exercise, but instructions below are given on how to test your code on your machine.

The goal is to have the output from the reducer with the following fields for each forum post:
"id"  "title"  "tagnames"  "author_id"  "node_type"  "parent_id"  "abs_parent_id"  "added_at"
"score"  "reputation"  "gold"  "silver"  "bronze"

Note that for each post we have taken some of the information describing the post,
and joined it with user information. The body of the post is not included in the final output.
The reason is that it is difficult to handle a multiline body, as it might be split on separate
lines during the intermediate steps Hadoop performs - shuffle and sort.

Your mapper code should take in records from both forum_node and forum_users.
It needs to keep, for each record, those fields that are needed for the final output given above.
In addition, mapper needs to add some text (e.g. "A" and "B") to mark where each output comes from
(user information vs forum post information). Example output from mapper is:

"12345"  "A"  "11"  "3"  "4"  "1"
"12345"  "B"   "6336" "Unit 1: Same Value Q"  "cs101 value same"  "question"  "\N"  "\N"  "2012-02-25 08:09:06.787181+00"  "1"

The first line originally comes from the forum_users input. It is from a student with user id: 12345 - the mapper key.
The next field is the marker A specifying that the record comes from forum_users.
What follows is the remaining information user information.

The second line originally comes from the forum_node input.
It also starts with the student id (mapper key) followed by a marker B and the information about the forum post.

The mapper key for both types of records is the student ID:
"user_ptr_id" from "forum_users" or  "author_id" from "forum_nodes" file.
Remember that during the sort and shuffle phases records will be grouped based on the student ID (12345 in our example).
You can use that to process and join the records appropriately in the reduce phase.
"""

import sys
import csv


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    hmap = {}
    A = 'A'
    B = 'B'

    for line in reader:
        # YOUR CODE HERE
        value = {}
        if len(line) == 5:
            data = [i for i in line[1:]]
            if line[0] in hmap:
                value = hmap[line[0]]
            value[A] = data
            hmap[line[0]] = value
        else:
            data = []
            for i in range(10):
                if i == 4 or i == 3:
                    continue
                data.append(line[i])
            if line[3] in hmap:
                value = hmap[line[3]]
            value[B] = data
            hmap[line[3]] = value
    for k,v in hmap.items():
        #print("%s \t %s" % (k, v))
        if A not in v or B not in v:
            continue
        op = [k, A]
        op.extend(v[A])
        op1 = [k, B]
        op1.extend(v[B])
        writer.writerow(op)
        writer.writerow(op1)


def main():
    mapper()


if __name__ == '__main__':
    main()