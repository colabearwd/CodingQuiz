# -*- coding:utf-8 -*-

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        height = len(array) - 1
        width = len(array[0]) - 1

        i = height
        j = 0

        while (j <= width) & (i >= 0):
            if target > array[i][j]:
                j+=1
            elif target < array[i][j]:
                i-=1
            else:
                return True
        return False