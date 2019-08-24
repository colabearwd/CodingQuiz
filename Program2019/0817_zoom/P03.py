import collections

if __name__ == '__main__':

    string = input()
    str_set = set(list(string))
    str_map = collections.OrderedDict()
    for val in string:
        if val not in str_map:
            str_map[val] = 1
        else:
            str_map[val] += 1
    end_key = list(str_map.keys())[-1]

    for key in str_map.keys():
        if key is not end_key:
            print('{}_{}_'.format(key, str_map[key]), end='')
        else:
            print('{}_{}'.format(key, str_map[key]), end='')


'''
abcdacbasdaeacadseadsacdsa

'''