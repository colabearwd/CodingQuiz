def count_num(mylist,i):
    count =0
    for x in mylist:
        if x == i:
            count += 1

    return count


if __name__ == '__main__':

    array = list(map(str, input().split(' ')))

    mylist = []

    for str in array:
        # print(str[0])
        # print(str[-1])
        mylist.append(str[0])
        mylist.append(str[-1])

    flag = True
    for i in mylist:
        res = count_num(mylist,i)

        if res % 2 != 0:
            flag = False
            break

    if flag:
        print('true')
    else:
        print('false')
