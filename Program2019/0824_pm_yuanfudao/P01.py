'''

3
3 1 1 1
3 2 2 3
4 0 2 3 99

'''


def justify_group(list1):
    count = 0
    for i in list1:
        if i != 0:
            count += 1
        else:
            continue
    if count >= 3:
        return True
    else:
        return False


def func02(group_num, group_list):
    next_index = []
    total = 0
    while justify_group(group_list):

        for i in range(group_num):
            if len(next_index) < 3:
                if group_list[i] > 0 and i not in next_index:
                    next_index.append(i)
            else:
                continue

        for i in next_index:
            group_list[i] -= 1

        next_index.clear()

        total+=1

    return total

def func01(mylist):
    # print(mylist)
    group_num = mylist[0]
    group_list = mylist[1:]

    if group_num < 3:
        return 0

    re = func02(group_num, group_list)

    return re


if __name__ == '__main__':
    loop = int(input())


    for i in range(loop):
        tmp_list = list(map(int, input().split()))
        re = func01(tmp_list)
        print(re)

