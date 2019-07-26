def ReverseNum(num):
    mylist = list(map(int, str(num)))
    print(mylist)

    otherlist = []
    for i in reversed(mylist):
        otherlist.append(i)
    print(otherlist)

    res = ''.join(str(x) for x in otherlist )
    print(int(res))

    return int(res)


def ReverseAdd(a, b):
    if a < 1 or a > 70000:
        return -1
    if b < 1 or b > 70000:
        return -1

    aa = ReverseNum(a)
    bb = ReverseNum(b)

    return aa + bb


if __name__ == '__main__':
    a, b = map(int, input().split(' '))
    print(a, b)

    # a, b = 100, 300

    res = ReverseAdd(a, b)
    print(res)