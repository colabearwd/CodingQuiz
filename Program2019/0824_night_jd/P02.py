def process(relation):
    count_dict = {}
    for tmp in relation:

        if tmp[0] in count_dict.keys():
            count_dict[tmp[0]] += 1
        else:
            count_dict.setdefault(tmp[0], 0)
            count_dict[tmp[0]] += 1

        if tmp[1] in count_dict.keys():
            count_dict[tmp[1]] += 1
        else:
            count_dict.setdefault(tmp[1], 0)
            count_dict[tmp[1]] += 1

    key_name = max(count_dict, key=count_dict.get)

    next_relation = []

    for tmp in relation:
        if tmp[0] == key_name or tmp[1] == key_name:
            continue
        else:
            next_relation.append(tmp)

    return key_name, next_relation

'''
2 2
1 3
1 4
'''
if __name__ == '__main__':
    n, m = map(int, input().split(" "))

    res_list = []

    relation = []

    for i in range(m):
        tmp = []
        a, b = map(int, input().split(" "))
        tmp.append(a)
        tmp.append(b)
        relation.append(tmp)

    while len(relation) > 0:
        key_name, next_relation = process(relation)
        res_list.append(key_name)
        relation = next_relation

    print(len(res_list))


    str_list = [str(x) for x in res_list]
    new_list = sorted(str_list)

    print(" ".join(str(x) for x in sorted(new_list)))
