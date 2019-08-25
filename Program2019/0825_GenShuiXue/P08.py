from math import sqrt


def prime_list(N):
    res = [p for p in range(2, N) if 0 not in [p % d for d in range(2, int(sqrt(p)) + 1)]]
    return res



if __name__ == '__main__':

    num = 100

    res_list = prime_list(num)

    for i in res_list:
        other = num - i
        if other in res_list:
            print(i, other)
            break
        else:
            continue
