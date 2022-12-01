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




