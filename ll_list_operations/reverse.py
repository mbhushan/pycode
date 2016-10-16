"""
 https://www.hackerrank.com/challenges/reverse-a-linked-list

 Reverse a linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def Reverse(head):
    if head is None or head.next is None:
        return head
    second = head.next
    head.next = None
    rest = Reverse(second)
    second.next = head
    return rest










