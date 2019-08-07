# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


t = TreeNode('#')


class Solution:
    def Level_Serialize_UseList(self, pRoot):
        if pRoot == None:
            return []

        level_queue = []
        node_stack = [pRoot]
        val_res = []

        while node_stack:
            temp_res = []
            next_stack = []

            for i in node_stack:
                temp_res.append(i.val)

                if (i.left is not None):
                    next_stack.append(i.left)

                if (i.right is not None):
                    next_stack.append(i.right)

            val_res.append(temp_res)
            node_stack = next_stack
        return val_res

    def Level_Serialize_UsePound(self, pRoot):
        if pRoot == None:
            return []

        node_queue = [pRoot]
        val_res = [pRoot.val]

        while node_queue:
            next_queue = []

            for node in node_queue:
                if node.left != None:
                    val_res.append(node.left.val)
                    next_queue.append(node.left)
                else:
                    val_res.append('#')

                if node.right != None:
                    val_res.append(node.right.val)
                    next_queue.append(node.right)
                else:
                    val_res.append('#')

            node_queue = next_queue
        return val_res

    # Pound 是'#'号
    def Level_Serialize_WithoutPound(self, pRoot):
        res = self.Level_Serialize_UsePound(pRoot)

        new_res = []

        for i in res:
            if i != '#':
                new_res.append(i)
            else:
                continue

        return new_res

    def Level_DeSerialize_UsePound(self, NodeValList):
        node_queue = []
        head = TreeNode(NodeValList[0])
        node_queue.append(head)

        i = 0
        while i < len(NodeValList):
            len_num = len(node_queue)

            for j in range(len_num):


                pass


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
    print(s.Level_Serialize_WithoutPound(head))

    print(s.Level_Serialize_UseList(head))

    print(s.Level_Serialize_UsePound(head))


