def which_index(arraya):
    for elem in arraya:
        index = arraya.index(elem)
        if elem > arraya[index + 1]:
            return index + 1

def justfy(arraya):
    is_sort = True
    for elem in arraya:
        index = arraya.index(elem)


def replace_num(arraya, arrayb, error_index):
    flag = False

    for num in reversed(arrayb):
        arraya[error_index] = num



if __name__ == '__main__':
    arraya = list(map(int, input().split(' ')))
    arrayb = list(map(int, input().split(' ')))
    arrayb = list(set(arrayb))

    error_index = which_index(arraya)

    replace_num(arraya, arrayb, error_index)
