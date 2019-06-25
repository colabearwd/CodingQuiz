

def func(num):
    if d[num] > 1:
        return d[num]

    if num == 0:
        return 0

    if num == 1 or num == 2:
        return 1

    d[num] = func(num - 1) + func(num - 2)

    return d[num]


if __name__ == '__main__':

    num = int(input())
    d = [1] * (num+1)

    a = func(num)

    print(a)
    print(d[1:])
