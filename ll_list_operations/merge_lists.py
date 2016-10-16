"""
https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists

 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node


def MergeLists(headA, headB):
    if headA is None and headB is None:
        return None
    if headA is None:
        return headB
    if headB is None:
        return headA

    node = Node()
    if headA.data <= headB.data:
        node = headA;
        node.next = MergeLists(headA.next, headB)
    else:
        node = headB;
        node.next = MergeLists(headA, headB.next)
    return node











