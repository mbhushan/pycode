"""
https://www.hackerrank.com/challenges/tree-inorder-traversal
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def inOrder(root):
    #Write your code here
    if root is None:
        return
    stack = []
    while stack or root:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            print(root.data, end=" ")
            root = root.right
