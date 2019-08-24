'''
计算绝对值
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 131072KB；其他语言 655360KB
题目描述：
给出n个正整数，要求找出相邻两个数字中差的绝对值最小的一对数字，如果有差的绝对值相同的，则输出最前面的一对数。

2<n<=100，正整数都在10^16范围内

输入
输入包含2行，第一行为n，第二行是n个用空格分隔的正整数。

输出
输出包含一行两个正整数，要求按照原来的顺序输出


样例输入
9
1 3 4 7 2 6 5 12 32
样例输出
3 4

'''
def myabs(str1,str2):
    a = [int(item) for item in str1]
    b = [int(item) for item in str2]

    res = ''
    for i in range(len(b)):
        flag_a = len(a) - 1 - i
        flag_b = len(b) - 1 - i

        if a[flag_a] >= b[flag_b]:
            res = str(a[flag_a] - b[flag_b]) + res
        else:
            res = str(10 + a[flag_a] - b[flag_b]) + res

            while a[flag_a - 1] == 0:
                a[flag_a - 1] = 9
                flag_a -= 1
            a[flag_a - 1] -= 1

        for j in range(len(a) - 1 - i - 1, -1, -1):
            res = str(a[j]) + res

        zero_flag = 0
        for i in range(len(res)):
            if res[i] != '0':
                zero_flag = 1
                break
        if zero_flag == 0:
            return 0
        return int(res[i:])




if __name__ == '__main__':
    num = int(input())
    num_list = list(map(str,input().split(' ')))

    index = 0
    if len(num_list[0]) > len(num_list[1]) or num_list[0] > num_list[1]:
        absmin =  abs(myabs(num_list[0],num_list[1]))
    else:
        absmin = abs(myabs(num_list[1], num_list[0]))

    for i in range(num-1):
        if len(num_list[i]) > len(num_list[i+1]) or num_list[i] > num_list[i+1]:
            tmpmin = abs(myabs(num_list[i],num_list[i+1]))
        else:
            tmpmin = abs(myabs(num_list[i+1], num_list[i]))


        if absmin == 0:
            break

        if tmpmin < absmin:
            index = i
            absmin =tmpmin
        else:
            continue

    print("{} {}".format(num_list[index],num_list[index+1]))
