import copy

COUNT = 0
mylist = []


def justify_str(tmplist):
    Flag = True

    for elem in tmplist:
        index = tmplist.index(elem)

        if index != len(tmplist) - 1:

            if tmplist[index][-1] != tmplist[index + 1][0]:
                Flag = False
            else:
                continue
        else:
            if tmplist[index][-1] != tmplist[0][0]:
                Flag = False
            else:
                continue

    return Flag


def perm(elem_list, begin, end):
    global COUNT

    if begin >= end:
        # print(elem_list)

        tmp = copy.deepcopy(elem_list)
        mylist.append(tmp)
        COUNT += 1

    else:
        i = begin
        for num in range(begin, end):
            elem_list[num], elem_list[i] = elem_list[i], elem_list[num]

            perm(elem_list, begin + 1, end)

            elem_list[num], elem_list[i] = elem_list[i], elem_list[num]


if __name__ == '__main__':
    # str_array = list(map(str, input().split(' ')))

    str_array = ['abc', 'cde', 'efa']

    perm(str_array, 0, len(str_array))
    print(mylist)

    have_circle = False
    for tmplist in mylist:
        if justify_str(tmplist):
            have_circle =True
    if have_circle:
        print('True')
    else:
        print('False')


