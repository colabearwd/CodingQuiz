def func01(array):
    lens = len(array)
    end = 1 << lens
    mark = 0

    val_res = []
    for i in range(lens + 1):
        val_res.append([])

    while mark < end:
        isNull = True
        i = 0

        tmp = []
        while i < lens:
            if 1 << i & mark:
                isNull = False
                tmp.append(array[i])
            i += 1

        # print(tmp)

        len_index = len(tmp)
        val_res[len_index].append(tmp)

        # if isNull:
        #     print("null")

        mark += 1

    return val_res


def func02(arrayList):
    lens = len(arrayList)

    end = 1 << lens
    mark = 0

    val_res = []
    for i in range(lens + 1):
        val_res.append([])

    while mark < end:
        isNull = True
        i = 0

        tmp = []

        for i in range(lens):
            if 1 << i & mark:
                isNull = False
                tmp.append(arrayList[i])

        len_index = len(tmp)
        val_res[len_index].append(tmp)

        mark += 1

    return val_res


if __name__ == '__main__':
    # n = ["aa","bb","cc"]

    n = [1, 2, 3, 4]
    res = func02(n)

    for i in res:
        print(i)
