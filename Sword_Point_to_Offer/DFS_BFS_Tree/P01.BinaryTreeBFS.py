# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bfs(node):
    if node is None:
        return
    queue = []

    val_list = []

    queue.append(node) # 当出现新元素的时候，添加到最后，相当于队尾

    while queue:
        cur = queue.pop(0)  # 弹出元素 #queue先进先出，queue的0就是先进入的部分，相当于队首
        val_list.append(cur.val)  # 元素值加入到队列
        if cur.left is not None:
            queue.append(cur.left)

        if cur.right is not None:
            queue.append(cur.right)

    return val_list


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

    res = bfs(head)

    print(res)
