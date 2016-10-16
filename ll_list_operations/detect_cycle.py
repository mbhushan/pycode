"""
https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle

Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as:

    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head is None:
        return False
    first = head
    second = head.next
    cycle = False
    while second:
        if second.next and second.next.next:
            second = second.next.next
        else:
            break
        first = first.next
        if first == second:
            cycle = True
            break
    return cycle


