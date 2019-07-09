def baseN(num, b):
    return ((num == 0) and "0") or (baseN(num // b, b).lstrip("0") + "0123456789abcdefghijklmnopqrstuvwxyz"[num % b])


def baseFunc(num, b):
    return ((num == 0) and '0') or (baseFunc(num // b, b).lstrip('0') + '0123456789abcdefghijklmnopqrstuvwxyz'[num % b])


if __name__ == '__main__':
    print(baseFunc(10, 2))
