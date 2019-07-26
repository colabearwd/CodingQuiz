def get_distinct_num(string):
    myset = set(map(int, string))
    mylist = list(myset)
    print(mylist)

    mylist = list(reversed(mylist))
    print(mylist)

    res = ''.join(str(x) for x in mylist)
    print(res)


if __name__ == '__main__':
    string = input()

    get_distinct_num(string)
