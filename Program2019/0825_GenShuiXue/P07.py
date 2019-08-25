def justify(Top5List, num):
    minnum = min(Top5List)

    if num > minnum:
        return True
    else:
        return False


def process(NumList):
    Top5List = []

    for i in NumList:
        if len(Top5List) < 5:
            Top5List.append(i)
        else:
            if justify(Top5List, i):
                minnum = min(Top5List)
                Top5List.remove(minnum)
                Top5List.append(i)
            else:
                continue

    sortedList = sorted(Top5List, reverse=True)
    # print(sortedList)
    print(sortedList[4])


if __name__ == '__main__':
    NumList = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 0, 10]
    process(NumList)
