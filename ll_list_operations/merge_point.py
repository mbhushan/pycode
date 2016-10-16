"""
https://www.hackerrank.com/challenges/find-the-merge-point-of-two-joined-linked-lists

 Find the node at which both lists merge and return the data of that node.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


"""


def FindMergeNode(headA, headB):
    first = headA
    lenA = 0
    while first:
        lenA = lenA + 1
        first = first.next
    first = headA
    lenB = 0
    second = headB
    while second:
        lenB = lenB + 1
        second = second.next
    second = headB

    while lenA > lenB:
        first = first.next
        lenA = lenA - 1
    while lenB > lenA:
        second = second.next
        lenB = lenB - 1
    while first != second:
        first = first.next
        second = second.next
    return first.data















