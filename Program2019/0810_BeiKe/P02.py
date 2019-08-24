'''
月光宝盒的密码
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 131072KB；其他语言 655360KB
题目描述：
小希偶然得到了传说中的月光宝盒,然而打开月光宝盒需要一串密码。虽然小希并不知道密码具体是什么，但是月光宝盒的说明书上有着一个长度为 n (2 <= N <= 50000)的序列 a (-10^9 <= a[i] <= 10^9)的范围内。下面写着一段话：密码是这个序列的最长的严格上升子序列的长度(严格上升子序列是指，子序列的元素是严格递增的，例如: [5,1,6,2,4]的最长严格上升子序列为[1,2,4])，请你帮小希找到这个密码。


输入
第1行：1个数N，N为序列的长度(2<=N<=50000)

第2到 N+1行：每行1个数，对应序列的元素(-10^9 <= a[i] <= 10^9)

输出
一个正整数表示严格最长上升子序列的长度


样例输入
8
5
1
6
8
2
4
5
10
样例输出
5

'''

if __name__ == '__main__':
    maxn = 50005
    INF = 0x7f7f7f7f

    lista = []
    listf = []

    n,ans = -INF,-INF

    num = int(input())
    for i in range(num):
        tmp = int(input())
        lista.append(tmp)
        listf.append(1)

    i = 1
    while i<num:
        j=1
        while j<i:
            if lista[j] < lista[i]:
                listf[i] = max(listf[i],listf[j]+1)
            j+=1
        i+=1

    for x,y in zip(lista,listf):
        ans = max(ans,y)
    print(ans)
