
def func01(str):
    num = 0
    res = 1
    for i in str:
        if i == '(':
            num += 1
        elif i == ')':
            res *= num
            num -= 1
    return res

if __name__ == '__main__':
    str = input()
    res = func01(str)
    print(res)