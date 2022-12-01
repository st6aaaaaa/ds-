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


