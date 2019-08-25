def func01(s: str):
    '''
    找出某个字符串所有的子串
    :param s:
    :return:
    '''
    results = []
    # x + 1 表示子字符串长度
    for x in range(len(s)):
        # i 表示偏移量
        tmp_res = []
        for i in range(len(s) - x):
            tmp_res.append(s[i:i + x + 1])
        results.append(tmp_res)
    return results





if __name__ == '__main__':
    str1='abcde'
    res = func01(str1)

    for i in res:
        print(i)

