# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths_01(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []

        if not root.left and not root.right:
            return [str(root.val)]

        pathList = []

        if root.left:
            pathList += self.binaryTreePaths_01(root.left)
        if root.right:
            pathList += self.binaryTreePaths_01(root.right)

        for index, path in enumerate(pathList):
            pathList[index] = str(root.val) + "->" + path

        return pathList

    def binaryTreePaths_02(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        pathList, stack = [], [(root, "")]
        while stack:
            node, pathStr = stack.pop(0)
            if not node.left and not node.right:
                pathList.append(pathStr + str(node.val))
            if node.left:
                stack.append((node.left, pathStr + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, pathStr + str(node.val) + "->"))
        return pathList


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

    res = s.binaryTreePaths_01(head)
    print(res)

    res = s.binaryTreePaths_02(head)
    print(res)