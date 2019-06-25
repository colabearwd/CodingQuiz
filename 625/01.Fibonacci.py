def func(num):
    if num == 0:
        return 0

    if num == 1 or num == 2:
        return 1

    return func(num - 1) + func(num - 2)


if __name__ == '__main__':
    num = int(input())
    print(func(num))
