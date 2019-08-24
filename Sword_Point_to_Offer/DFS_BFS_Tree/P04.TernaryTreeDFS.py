# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.center = None
        self.right = None


val_res = []


def DFS_Recursive(pRoot):
    if (pRoot == None):
        return

    val_res.append(pRoot.val)
    # print(pRoot.val)

    if (pRoot.left != None):
        DFS_Recursive(pRoot.left)

    if (pRoot.center != None):
        DFS_Recursive(pRoot.center)

    if (pRoot.right != None):
        DFS_Recursive(pRoot.right)


if __name__ == '__main__':
    head = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n8 = TreeNode(8)

    t10 = TreeNode(10)
    t11 = TreeNode(11)
    t12 = TreeNode(12)
    t13 = TreeNode(13)

    head.left = n2
    n2.left = n4
    head.right = n3
    n3.left = n5
    n3.right = n6
    n5.left = n7
    n5.right = n8

    n2.center = t10
    n3.center = t11
    n7.center = t12
    n6.center = t13

    DFS_Recursive(head)

    print(val_res)
