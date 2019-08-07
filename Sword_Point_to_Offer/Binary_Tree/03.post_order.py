# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
val_res=[]
class Solution:
    def Post_Order(self, pRoot):
        # write code here
        if pRoot.left:
            self.Post_Order(pRoot.left)
        if pRoot.right:
            self.Post_Order(pRoot.right)
        # print(pRoot.val)
        val_res.append(pRoot.val)

        return val_res

    def Post_Order_non_recursion(self, pRoot):
        if pRoot == None:
            return
        res = []
        stack = []
        node = pRoot

        while stack or node:
            while node:
                res.append(node.val)
                stack.append(node)
                node = node.right
            if stack:
                top = stack.pop()
                node = top.left
        return res[::-1]


if __name__ == '__main__':

    head = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)
    head.left = n2
    n2.left = n4
    head.right = n3
    n3.left = n5
    n3.right = n6
    n5.left = n7
    n5.right = n8

    s = Solution()
    res = s.Post_Order(head)
    print(res)

    res = s.Post_Order_non_recursion(head)
    print(res)

