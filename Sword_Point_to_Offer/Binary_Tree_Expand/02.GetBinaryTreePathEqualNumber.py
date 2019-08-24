# -*- coding:utf-8 -*-
class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def function(root, target_number):
    result = []
    if not root:
        return result
    #  如果只有根节点或者找到叶子节点，我们就把其值返回
    if not root.left and not root.right and root.val == target_number:
        return [[root.val]]

    else:
        #  如果不是叶子节点，我们分别对根节点的左子树、右子树进行递归，注意修改变量:
        left = function(root.left, target_number - root.val)
        right = function(root.right, target_number - root.val)
        for item in left + right:
            result.append([root.val] + item)

    return result

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

    res = function(head,7)
    print(res)