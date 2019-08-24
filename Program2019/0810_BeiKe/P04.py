'''
特殊的测试
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 131072KB；其他语言 655360KB
题目描述：
小C在做一种特殊的服务器负载测试，对于一个请求队列中的请求，每一个请求都有一个负荷值，为了保证服务器稳定，请求队列中的请求负荷必须按照先递增后递减的规律(仅递增，仅递减也可以)，比如[ 1，2，8，4，3 ]，[ 1，3，5 ]和[ 10 ]这些是满足规律的，还有一些不满足的，比如[ 1，2，2，1 ]，[ 2，1，2 ]和[ 10，10 ]。现在给你一个请求队列，你可以对请求的负荷值进行增加，要求你调整队列中请求的负荷值，使数组满足条件。最后输出使队列满足条件最小的增加总和。

输入
输入有两行，第一行是N (1≤n≤5000) ，代表请求队列中的请求数量。

第二行有N个数字 a1,a2…an  (1≤ai≤10^9)。Ai是第i个请求的负荷值。

输出
输出这个最小增加总和


样例输入
5
1 4 3 2 5
样例输出
6

提示
样例解释，此时合法队列为[1,4,5,6,5]，最小增加和为6
'''
import copy


def verify_up(tmplist):
    i = 0
    lens = len(tmplist)
    flag = True
    while i < lens - 1:
        if tmplist[i] > tmplist[i + 1]:
            continue
        else:
            flag = False

    return flag


def verify_down(tmplist):
    i = 0
    lens = len(tmplist)
    flag = True
    while i < lens - 1:
        if tmplist[i] < tmplist[i + 1]:
            continue
        else:
            flag = False

    return flag


if __name__ == '__main__':
    num = int(input())
    num_list = list(map(int, input().split(' ')))

    tmp_list = copy.deepcopy(num_list)
    tmp_list.sort()

