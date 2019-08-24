'''
举重大赛
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 131072KB；其他语言 655360KB
题目描述：
举重大赛开始了，为了保证公平，要求比赛的双方体重较小值要大于等于较大值的90%，那么对于这N个人最多能进行多少场比赛呢，任意两人之间最多进行一场比赛。

输入
第一行N，表示参赛人数（2<=N<=10^5）

第二行N个正整数表示体重（0<体重<=10^8）

输出
一个数，表示最多能进行的比赛场数


样例输入
5
1 1 1 1 1
样例输出
10
'''

if __name__ == '__main__':
    num = int(input())
    num_list = list(map(int, input().split(' ')))

    val_res = []

    for i in range(num):
        tmp = [0] * num
        val_res.append(tmp)

    # print(val_res)

    # for x in num_list:
    #     for y in num_list:
    #         xindex = num_list.index(x)
    #         yindex = num_list.index(y)
    #         print(xindex,yindex)
    #         if xindex != yindex:
    #             if x > y:
    #                if y >= x * 0.9 :
    #                    val_res[xindex][yindex] = 1
    #                    val_res[yindex][xindex] = 1
    #                else:
    #                    continue
    #             else:
    #                 if x >= y * 0.9:
    #                     val_res[xindex][yindex] = 1
    #                     val_res[yindex][xindex] = 1
    #                 else:
    #                     continue

    i=0
    while i < num:
        j=0
        while j< num:
            if i != j:
                x = num_list[i]
                y= num_list[j]

                if x > y:
                    if y >= x * 0.9:
                        val_res[i][j] = 1
                        val_res[j][i] = 1
                    else:
                        continue
                else:
                    if x >= y * 0.9:
                        val_res[i][j] = 1
                        val_res[j][i] = 1
                    else:
                        continue
            j+=1
        i+=1


    # print(val_res)

    count = 0
    for i in val_res:
        for j in i:
            count+=j
    print(int(count/2))


