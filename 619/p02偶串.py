'''
题目描述：
    如果一个字符串由两个相同字符串连接而成,就称这个字符串是偶串。
    例如"xyzxyz"和"aaaaaa"是偶串,但是"ababab"和"xyzxy"却不是。
    牛牛现在给你一个只包含小写字母的偶串s,你可以从字符串s的末尾删除1和或者多个字符,保证删除之后的字符串还是一个偶串,牛牛想知道删除之后得到最长偶串长度是多少。
输入描述:
    输入包括一个字符串s,字符串长度length(2 ≤ length ≤ 200),保证s是一个偶串且由小写字母构成
输出描述:
    输出一个整数,表示删除之后能得到的最长偶串长度是多少。保证测试数据有非零解
示例1
输入
    abaababaab
输出
    6
分析思路：
    枚举最后得到的偶串的长度,然后暴力去check是否是偶串。这里是倒着枚举的所以得到的第一个满足条件的即是所求答案

'''

if __name__ == '__main__':
    str = input()
    slen = int((len(str) - 1) / 2)

    while slen >= 1:
        is_event_str = True
        for i in range(slen):
            if str[i] != str[slen + i]:
                is_event_str = False
                break

        if is_event_str:
            print(slen * 2)

        slen -= 1
