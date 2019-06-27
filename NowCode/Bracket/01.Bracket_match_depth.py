
def func01(str):
    num = 0
    record = num
    for i in str:
        if i == '(':
            num += 1
        elif i == ')':
            num -= 1
        if num > record:
            record = num

    return record

if __name__ == '__main__':
    str = input()
    res = func01(str)
    print(res)