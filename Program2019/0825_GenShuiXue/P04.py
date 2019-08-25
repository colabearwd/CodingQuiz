def process(matrix, num):
    flag = True
    for i in range(num):
        for j in range(num):
            if i == j:
                continue
            elif matrix[i][j] != matrix[j][i]:
                flag = False
            else:
                continue

    return flag


if __name__ == '__main__':
    matrix = [[0, 1, 2, 3, 4], [1, 0, 1, 2, 3], [2, 1, 0, 1, 2], [3, 2, 1, 0, 1], [4, 3, 2, 1, 0]]
    num = 5

    f = process(matrix, num)
    print(f)
