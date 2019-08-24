def justify_list(tmp1, tmp2):
    flag = True

    for i in tmp1:
        if i not in tmp2:
            flag = False
        else:
            continue

    return flag


def func01(person_list, sorted_list, person_count):
    total = 0

    i = 0

    while i < person_count:

        cur = 1
        while cur <= (person_count - i):
            tmp1 = person_list[i:i + cur]
            tmp2 = sorted_list[i:i + cur]

            print(tmp1, tmp2)
            if justify_list(tmp1, tmp2):
                total += 1
                i = i + cur
                break
            else:
                cur += 1
        # print(i, cur)
        # input()


    print(total)
    # return total


def process(person_count, person_list):
    sorted_list = sorted(person_list)
    # print(person_list)
    # print(sorted_list)

    func01(person_list, sorted_list, person_count)


if __name__ == '__main__':
    # person_count = int(input())
    #
    # person_list = list(map(int, input().split(' ')))

    person_count = 10

    person_list = [69079936, 236011312, 77957850, 653604087, 443890802, 277126428, 755625552, 768751840, 993860213,
                   882053548]

    process(person_count, person_list)
