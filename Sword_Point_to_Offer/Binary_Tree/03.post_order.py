# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def Pre_Print(self, pRoot):
        # write code here
        if pRoot.left:
            self.Pre_Print(self,pRoot.left)
        if pRoot.right:
            self.Pre_Print(self,pRoot.right)

        print(pRoot.val)

        return