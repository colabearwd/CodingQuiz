import functools

def mycmp(num1,num2):
    str1 = str(num1) + str(num2)
    str2 = str(num2) + str(num1)

    # print(str1, str2)

    # 判断哪一个组成的数字大，
    # 如果
    # str1大，返回-1
    # str2大，返回1
    if int(str1) < int(str2):
        return 1
    else:
        return -1


def process(mylist):
    # 得到str的list
    str_list = [str(x) for x in mylist]

    # 对其进行字符排序
    str_list.sort()
    # 对字符排序进行设置
    str_list.sort(key=functools.cmp_to_key(mycmp),reverse=True)

    # 逆序打印
    print("".join(reversed(str_list)))


if __name__ == '__main__':
    # mylist = list(map(int,input().split(' ')))

    mylist1 = [12, 15, 666, 777]

    mylist2 = [3, 5, 34, 30, 9,300]

    process(mylist2)