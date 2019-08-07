# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def Pre_Serialize(self, root):
        if not root:
            return '#'
        return str(root.val) + ',' + self.Pre_Serialize(root.left) + ',' + self.Pre_Serialize(root.right)

    def In_Serialize(self, root):
        if not root:
            return '#'
        return self.In_Serialize(root.left) + ',' + str(root.val) + ',' + self.In_Serialize(root.right)

    def Post_Serialize(self, root):
        if not root:
            return '#'
        return self.Post_Serialize(root.left) + ',' + self.Post_Serialize(root.right) + ',' + str(root.val)

    def Pre_Deserialize(self, s):
        list = s.split(',')
        return self.Pre_deserializeTree(list)

    def Pre_deserializeTree(self, list):
        if len(list) <= 0:
            return None
        val = list.pop(0)
        root = None
        if val != '#':
            root = TreeNode(int(val))
            root.left = self.Pre_deserializeTree(list)
            root.right = self.Pre_deserializeTree(list)
        return root

    def In_Deserialize(self, s):
        list = s.split(',')
        return self.In_deserializeTree(list)

    def In_deserializeTree(self, list):
        if len(list) <= 0:
            return None
        val = list.pop(0)
        root = None
        if val != '#':
            root.left = self.In_deserializeTree(list)
            root = TreeNode(int(val))
            root.right = self.In_deserializeTree(list)
        return root

    def Post_Deserialize(self, s):
        list = s.split(',')
        return self.Post_deserializeTree(list)

    def Post_deserializeTree(self, list):
        if len(list) <= 0:
            return None
        val = list.pop(0)
        root = None
        if val != '#':
            root.left = self.Post_deserializeTree(list)
            root.right = self.Post_deserializeTree(list)
            root = TreeNode(int(val))
        return root


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

    prestr = s.Pre_Serialize(head)
    instr = s.In_Serialize(head)
    poststr = s.Post_Serialize(head)

    print(prestr)
    print(instr)
    print(poststr)
