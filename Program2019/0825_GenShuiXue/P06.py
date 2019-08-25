class Solution:
    def count_changes(self, N):
        v1, v5, v10, v20 = 0, 0, 0, 0
        if N >= 20:
            v20 += N // 20
            N = N % 20
        if N >= 10:
            v10 += N // 10
            N = N % 10
        if N >= 5:
            v5 += N // 5
            N = N % 5
        if N >= 1:
            v1 += N
        return v1, v5, v10, v20


if __name__ == '__main__':
    s =Solution()

    v1, v5, v10, v20 = s.count_changes(100)

    print(v1, v5, v10, v20)