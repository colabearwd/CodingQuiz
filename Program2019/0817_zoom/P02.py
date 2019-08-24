def baseFunc(num, b):
    return ((num == 0) and '0') or (baseFunc(num // b, b).lstrip('0') + '0123456789abcdefghijklmnopqrstuvwxyz'[num % b])

my_dict = {}

def func01(N,tmp):



    # xor_res = int(baseFunc(N,2)) ^ int(baseFunc(tmp,2))
    xor_res = N ^ tmp

    print(int(baseFunc(N, 2)), int(baseFunc(tmp, 2)) , int(baseFunc(xor_res, 2)))

    count = 0
    for i in str(bin(xor_res).replace('0b','')):
        if i == '1':
            count+=1
        else:
            continue

    print(N,tmp,count)

    my_dict.setdefault(count,[])
    my_dict[count].append(int(tmp))

'''
10
1 2 3 4 5 6 7 8 9 10
'''


if __name__ == '__main__':
    N = int(input())
    N_list = list(map(int,input().split()))



    for tmp in N_list:

        func01(int(N),int(tmp))

    print(my_dict)

