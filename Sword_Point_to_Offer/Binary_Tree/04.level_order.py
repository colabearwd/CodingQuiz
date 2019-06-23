# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def Level_Print(self, pRoot):
        if pRoot == None:
            return
        stack1 = [pRoot]
        stack2 = [pRoot]

        while stack1:
            node = stack1.pop(0)
            if node.left:
                stack1.append(node.left)
                stack2.append(node.left)
            if node.right:
                stack1.append(node.right)
                stack2.append(node.right)

        while stack2:
            print(stack2.pop(0).val)


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

Solution.Level_Print(Solution, head)
