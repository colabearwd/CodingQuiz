
def func01(str):
    num = 0

    for i in str:
        if i == '(':
            num += 1
        elif i == ')':
            num -= 1
        if num < 0 :
            return False

    if num == 0:
        return True
    else:
        return False

def test_func01():
    test_items = [
        ('(())',True),
        ('((())',False),
        ('()()((())))',False)
    ]
    for item in test_items:
        data,expected =item

        res = func01(data)

        e = "ERROR ! ({}),({}),({})".format(data,expected,res)
        assert res == expected,e

if __name__ == '__main__':
    # str = input()
    # res = func01(str)
    # print(res)

    test_func01()