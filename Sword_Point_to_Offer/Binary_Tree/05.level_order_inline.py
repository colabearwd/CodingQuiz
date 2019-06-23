# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Level_Print(self,pRoot):
        if pRoot == None:
            return []

        node_stack = [ pRoot ]
        val_res = []

        while node_stack:
            temp_res = []
            next_stack = []
            for i in  node_stack:
                temp_res.append(i.val)
                if i.left:
                    next_stack.append(i.left)
                if i.right:
                    next_stack.append(i.right)
            val_res.append(temp_res)
            node_stack = next_stack

        return val_res






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

res = Solution.Level_Print(Solution,head)

print(res)

for re in res:
    print(' '.join(str(i) for i in re))
