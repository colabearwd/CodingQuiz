import copy
def which_index(arraya):
    for elem in arraya:
        index = arraya.index(elem)
        if elem > arraya[index + 1]:
            return index + 1

def justfy(arraya):
    is_sort = True

    tmp = copy.deepcopy(arraya)
    tmp.sort()
    for i,j in zip(tmp,arraya):
        if i!=j:
            is_sort=False
        else:
            continue
    return is_sort


def replace_num(arraya, arrayb, error_index):
    flag = False

    for num in reversed(arrayb):
        # print(arraya)
        arraya[error_index] = num

        if justfy(arraya):
            return arraya
        else:
            continue

    return 'NO'



if __name__ == '__main__':
    arraya = list(map(int, input().split(' ')))
    arrayb = list(map(int, input().split(' ')))

    # arraya = [1, 3, 7, 4, 10]
    # arraya = [1, 3, 7, 13, 12]
    # arraya = [4, 3, 7, 8, 10]
    # arraya = [1, 3, 7, 11, 10]
    # arraya = [1, 3, 7, 16, 9]

    # arrayb = [2, 1, 5, 8, 9, 14]

    arrayb = list(set(arrayb))

    error_index = which_index(arraya)
    # print(error_index)

    res = replace_num(arraya, arrayb, error_index)
    print(res)

