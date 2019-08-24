def func01(my_str):
    length = len(my_str)

    c = my_str[0]
    num = 1
    flag = True

    i = 1
    while i < length:
        if my_str[i] == c:
            flag = False
            num += 1
        else:
            if flag:
                print(c)
            else:
                print("{}_{}".format(c, num), end='_')
            num = 1
            c = my_str[i]
            flag = True

        i += 1

    if not flag:
        print("{}_{}".format(c, num))
    else:
        print(c)


if __name__ == '__main__':
    # mystr = str(input())
    mystr = 'aaaabbbcccccdddeeeeeee'

    func01(mystr)
