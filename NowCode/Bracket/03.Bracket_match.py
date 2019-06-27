def func01(str):
    L, R = 0, 0
    for i in str:
        if i == '[':
            L += 1
        elif i == ']':
            if L > 0:
                L -= 1
            else:
                R += 1

    new = '[' * R + str + ']' * L

    # print(new)
    return new

if __name__ == '__main__':
    str = input()
    res = func01(str)
    print(res)
