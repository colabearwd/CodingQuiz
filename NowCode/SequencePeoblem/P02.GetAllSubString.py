def GetSubString(s: str):
    results = []
    # x + 1 表示子字符串长度
    for x in range(len(s)):
        # i 表示偏移量
        for i in range(len(s) - x):
            tmp = s[i:i + x + 1]
            length = len(tmp)
            val_res[length].append(tmp)
    return val_res


if __name__ == '__main__':
    str1 = 'abcde'

    val_res = []
    for i in range(len(str1)+1):
        val_res.append([])

    res = GetSubString(str1)
    for re in res:
        print(re)
