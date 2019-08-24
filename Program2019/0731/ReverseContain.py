'''
作者：求上进
链接：https://www.nowcoder.com/discuss/214009
来源：牛客网

题目：判断一个旋转字符串是否可以包含另一个字符串。
旋转字符串举例：AABC -> BCAA
输入：
AABC
ABCA
ABFSR
FS
UYT
HY
每次三组测试样例，奇数行为源字符串，偶数行为目标字符串，包含为1.
如上例输出为110
'''

'''
只通过了85.75%case,
返回是数组越界
不知道是不是需要添加strip
'''

def func01(str1, str2):

    if  len(str2)>len(str1):
        return 0

    new_str1 = "{}{}".format(str1, str1)

    if str2 in new_str1:
        return 1
    else:
        return 0


if __name__ == '__main__':
    str1 = input().strip()
    str2 = input().strip()
    str3 = input().strip()
    str4 = input().strip()
    str5 = input().strip()
    str6 = input().strip()



    res1 = func01(str1, str2)
    res2 = func01(str3, str4)
    res3 = func01(str5, str6)

    print("{}{}{}".format(res1,res2,res3),end='')
