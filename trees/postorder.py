# https://www.hackerrank.com/challenges/tree-postorder-traversal
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def postOrder(root):
    #Write your code here
    if root is None:
        return
    if root.left:
        postOrder(root.left)
    if root.right:
        postOrder(root.right)
    print(root.data, end=" ")