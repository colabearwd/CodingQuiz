def func01(my_str):
    length = len(my_str)

    c = my_str[0]
    num = 1

    i = 1
    while i < length:
        if my_str[i] == c:

            num += 1
        else:
            print(c, end='')
            num = 1
            c = my_str[i]

        i += 1

    print(c, end='')


if __name__ == '__main__':
    mystr = str(input())
    # mystr = 'AABBBCCDDAA'

    func01(mystr)
