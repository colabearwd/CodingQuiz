def perm(elem_list, begin, end):
    '''
    找出这个序列的所有可能排序
    :param elem_list: 序列全部数据
    :param begin: 起始点
    :param end: 结束点
    :return:
    '''
    if begin >= end:
        print(elem_list)

    else:
        i = begin
        for num in range(begin, end):
            elem_list[num], elem_list[i] = elem_list[i], elem_list[num]

            perm(elem_list, begin + 1, end)

            elem_list[num], elem_list[i] = elem_list[i], elem_list[num]


if __name__ == '__main__':
    # n = [1, 2, 3]

    n = ['aa','bb','cc']
    perm(n, 0, len(n))

