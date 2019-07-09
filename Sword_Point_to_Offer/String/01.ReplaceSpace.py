# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        # write code here
        replace_str = '%20'
        temp = ''
        for i in s:
            if i == ' ':
                temp = temp + replace_str
            else:
                temp = temp + i

        print(temp)
        return temp

if __name__ == '__main__':
    # str = "We Are Happy"
    str = "hello world"
    Solution.replaceSpace(Solution,str)