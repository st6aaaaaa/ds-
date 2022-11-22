'''You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return
the subtree rooted with that node. If such a node does not exist, return null.'''

# first solution


def func(root,val):
    if root is None:
        return None
    if root.val == val:
        return root
    else :
        if root.val < val:
            return func(root.right,val)
        else:
            return func(root.left,val)

# second solution

def func(root,val):
    stack = []
    subtree = None

    while True :
        while root :
            if root.val == val : return root
            stack.append(root)
            root = root.left
        if not stack: return None
        stack.pop().right
