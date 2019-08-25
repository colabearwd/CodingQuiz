

def GetSubSequences(chars, index, res):
    if (index == len(chars)):

        resLen = len(res)
        if resLen > 0:
            val_res[resLen].append(res)
        return

    GetSubSequences(chars, index + 1, res)
    GetSubSequences(chars, index + 1, res + chars[index])


if __name__ == '__main__':

    str1 = 'abcde'

    val_res = []
    for i in range(len(str1)+1):
        val_res.append([])

    GetSubSequences(str1, 0, "")

    for i in val_res:
        print(i)