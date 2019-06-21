'''
题目描述：4位的密码，每一位的值为a-e，写出所有的可能
分析思路：

'''



str='abcde'


def gen_passwd():
    for i in str:
        for j in str:
            for m in str:
                for n in str:
                    print('{}{}{}{}'.format(i,j,m,n))

if __name__ == '__main__':
    gen_passwd()