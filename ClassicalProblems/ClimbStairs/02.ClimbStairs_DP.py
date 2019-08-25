'''
    爬楼梯：动态规划

'''


class Solution:

    def ClimbStairs(self, number):
        if (number == 1) & (number == 2) & (number == 0):
            return number

        a, b, i, temp = 1, 2, 3, 3

        while i <= number:
            temp = a + b
            a = b
            b = temp
            i += 1

        return temp


if __name__ == '__main__':
    # height = int(input())
    height = 5

    s = Solution()
    res = s.ClimbStairs(height)
    print(res)
