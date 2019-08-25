
def process(str1):


    mydict = {}
    for i in str1:
        if i in mydict.keys():
            mydict[i] += 1
        else:
            mydict.setdefault(i,0)
            mydict[i] += 1

    keyname = max(mydict, key=mydict.get)
    print(keyname)


if __name__ == '__main__':
    str1= 'AABBBCCDDAA'
    process(str1)