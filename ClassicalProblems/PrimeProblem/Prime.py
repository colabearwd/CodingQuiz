from math import sqrt


def isPrime_01(n):
    '''
    Use math.sqrt
    '''
    if n <= 1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def isPrime_02(n):
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def isPrime_03(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def primeList(N):
    res = [p for p in range(2, N) if 0 not in [p % d for d in range(2, int(sqrt(p)) + 1)]]
    return res


if __name__ == '__main__':
    print(primeList(1000))

    n = 3
    print(isPrime_01(n))
    print(isPrime_02(n))
    print(isPrime_03(n))
