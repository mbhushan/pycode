"""
https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list

 Delete Node at a given position in a linked list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""


def Delete(head, position):
    if head is None:
        return head

    if position == 0:
        head = head.next
    else:
        curr = head
        count = 1
        while count < position:
            count = count + 1
            curr = curr.next
        node = curr.next
        if node.next:
            curr.next = node.next
        else:
            curr.next = None
        node.next = None
    return head





