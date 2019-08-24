# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.center = None
        self.right = None

def bfs(node):
    if node is None:
        return
    queue = []

    val_list = []

    queue.insert(0, node)

    while queue:
        cur = queue.pop()  # 弹出元素
        val_list.append(cur.val)  # 元素值加入到队列
        if cur.left is not None:
            queue.insert(0, cur.left)

        if cur.center is not None:
            queue.insert(0, cur.center)

        if cur.right is not None:
            queue.insert(0, cur.right)

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

    res = bfs(head)

    print(res)