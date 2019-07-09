# -*- coding:utf-8 -*-
class Solution:

    def __init__(self):
        self.str = ''
        self.hash_list = [0]*256

    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        for i in self.str:
            if self.hash_list[ord(i)] == 1:
                return i
        return '#'


    def Insert(self, char):
        # write code here
        self.str+=char
        self.hash_list[ord(char)] += 1

if __name__ == '__main__':
    str1 = 'go'
    str2 = 'google'
    s = Solution()

    for i in str2:
        s.Insert(i)

    res = s.FirstAppearingOnce()

    print(res)