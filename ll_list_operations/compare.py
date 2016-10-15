"""
https://www.hackerrank.com/challenges/compare-two-linked-lists
 Merge two linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def CompareLists(headA, headB):
    A = headA
    B = headB
    ans = compare(A, B)
    if ans:
        return 1
    else:
        return 0


def compare(A, B):
    if A is None and B is None:
        return True
    if A is None or B is None:
        return False

    flag = False
    if A.data == B.data:
        flag = compare(A.next, B.next)
        if flag:
            return True
    else:
        return False
    return flag













