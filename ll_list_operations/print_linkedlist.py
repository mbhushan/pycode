class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList(object):

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert_tail(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = node

    def print_list(self):
        node = self.head
        while  node:
            print(node.data)
            node = node.next


def main():
    ll = LinkedList()
    n = 5
    for i in range(n):
        #ll.insert(i+1)
        ll.insert_tail(i+1)
    ll.print_list()

if __name__ == '__main__':
    main()


