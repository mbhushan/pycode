"""
https://www.hackerrank.com/challenges/delete-duplicate-value-nodes-from-a-sorted-linked-list

 Delete duplicate nodes
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def RemoveDuplicates(head):
    if head is None or head.next is None:
        return head
    node = head
    prev = head.data
    while node.next:
        if node.next.data == prev:
            node.next = node.next.next
        else:
            prev = node.next.data
            node = node.next
    return head










