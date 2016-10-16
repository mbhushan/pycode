"""
https://www.hackerrank.com/challenges/insert-a-node-into-a-sorted-doubly-linked-list

 Insert a node into a sorted doubly linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None, prev_node = None):
       self.data = data
       self.next = next_node
       self.prev = prev_node

 return the head node of the updated list
"""


class Node(object):
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node


def SortedInsert(head, data):
    node = Node(data)
    if head is None:
        head = node
        return head
    # first node
    if data <= head.data:
        node.next = head
        head.prev = node
        head = node
    curr = head
    while curr.next and curr.next.data < data:
        curr = curr.next
    if curr.next:
        node.next = curr.next
        node.prev = curr
        curr.next.prev = node
        curr.next = node
    else:
        curr.next = node
        node.prev = curr
    return head











