def perm(elem_list, begin, end):
    if begin >= end:
        print(elem_list)

    else:
        i = begin
        for num in range(begin, end):
            elem_list[num], elem_list[i] = elem_list[i], elem_list[num]

            perm(elem_list, begin + 1, end)

            elem_list[num], elem_list[i] = elem_list[i], elem_list[num]


if __name__ == '__main__':
    n = [1, 2, 3]
    perm(n, 0, len(n))
