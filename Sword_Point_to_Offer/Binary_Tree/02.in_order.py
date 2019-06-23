# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def In_Order(self, pRoot):
        # write code here
        if pRoot.left:
            self.In_Order(self,pRoot.left)
        print(pRoot.val)
        if pRoot.right:
            self.In_Order(self,pRoot.right)
        return

    def In_Order_non_recursion(self,pRoot):
        if pRoot == None:
            return
        res = []
        stack = []
        node = pRoot

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                res.append(node.val)
                node = node.right
        print(res)
        return res

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

Solution.In_Order_non_recursion(Solution,head)

