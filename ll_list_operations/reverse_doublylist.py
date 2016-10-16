"""
https://www.hackerrank.com/challenges/reverse-a-doubly-linked-list

 Reverse a doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list
"""


def Reverse(head):
    if head is None or head.next is None:
        return head
    second = head.next
    head.next.prev = None
    head.next = None
    rest = Reverse(second)
    second.next = head
    head.prev = second
    return rest








