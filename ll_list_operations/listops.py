"""
https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list

 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


# This is a "method-only" submission.
# You only need to complete this method.
def InsertNth(head, data, position):
    node = Node(data)
    if position == 0:
        node.next = head
        head = node
    else:
        curr = head
        count = 1
        while count < position:
            curr = curr.next
            count = count + 1
        node.next = curr.next
        curr.next = node
    return head