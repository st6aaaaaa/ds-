'''Given the root of a binary tree, return the
inorder traversal of its nodes' values.'''


class Solution:
    def inorderTraversal(root):
        def func(node, arr):
            if node is not None:
                func(node.left, arr)
                arr.append(node.val)
                func(node.right, arr)

        arr = []
        func(root, arr)
        return arr


    ### ########################   second solution
        if root is None:
            return []

        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right)


    ############################  third

        res  = []
        stack = []
        cur = root
        while cur or stack:
            while cur :
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res


'''Given the root of a binary tree, check whether it is 
a mirror of itself (i.e., symmetric around its center).'''


def isSymmetric( root) -> bool:
    def mirror(t1, t2):
        if t1 is None and not t2:
            return True
        if t1 is None and t2 or t1 and not t2:
            return False

        return t1.val == t2.val and mirror(t1.left, t2.right) and mirror(t2.left, t1.right)

    return mirror(root, root)

################  second solution


    d = deque()
    d.append(root)
    d.append(root)
    while d:
        t1 = d.pop()
        t2 = d.pop()
        if t1 is None and t2 is None:
            continue
        if t1 is None and t2 or t2 is None and t1:
            return False
        if t1.val != t2.val:
            return False
        d.append(t1.left)
        d.append(t2.right)
        d.append(t1.right)
        d.append(t2.left)
    return True


'''Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced
 binary search tree.'''

class TreeNode:
    def __init__(self,val=0,left = None , right = None ):
        self.val = val
        self.right = right
        self.left = left
def sortedArrayToBST(nums):
    def func(low, high):
        if low > high:
            return None
        else:
            mid = (low + high) // 2
            root = TreeNode(nums[mid])
            root.left = func(low, mid - 1)
            root.right = func(mid + 1, high)
            return root

    return func(0, len(nums) - 1)
### second solution
    if len(nums) == 0:
        return None
    mid = len(nums) // 2
    return TreeNode(nums[mid], self.sortedArrayToBST(nums[:mid]), self.sortedArrayToBST(nums[mid + 1:]))


'''Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

'''


def sumOfLeftLeaves(root,isleft ):
    if root.left is None and root.right is None:
        return 0
    if root and root.left is None and root.right is None :
        return root.val if isleft else 0
    sum = 0
    if root.left :
        sum+=sumOfLeftLeaves(root.left,True)
    if root.right :
        sum+=sumOfLeftLeaves(root.right,False)
    return sum


def sumOfLeftLeaves(root):
    if root.left is None and root.right is None:
        return 0

    def func(node):
        return node and not node.left and not node.right

    sum = 0
    stack = [root]
    while stack :
        cur = stack.pop()
        if func(cur.left):
            sum+=cur.left.val
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return sum
