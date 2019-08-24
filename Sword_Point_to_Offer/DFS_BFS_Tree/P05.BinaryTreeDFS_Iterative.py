# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def DFS_Iterative(pRoot):
    if pRoot == None:
        return

    stack = []

    stack.append(pRoot)

    while len(stack) != 0:

        tmpNode = stack[-1]
        print(tmpNode.val)

        stack.remove(tmpNode)

        if tmpNode.right != None:
            stack.append(tmpNode.right)

        if tmpNode.left != None:
            stack.append(tmpNode.left)



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

    DFS_Iterative(head)

    # print(val_res)

