
def process(ary,N):
    ary_set = set(ary)
    if len(ary_set) <5 :
        return -1
    ary_set_list = list(ary_set)
    ary_set_list.sort()
    return ary_set_list[-5]

if __name__ == '__main__':
    NumList = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 0, 10]
    re = process(NumList,len(NumList))

    print(re)
    print(sorted(NumList))