'''
    爬楼梯，备忘录法
'''


class Solution:
    def __init__(self):
        self.mem_list = [0] * 500
        self.mem_list[0] = 0
        self.mem_list[1] = 1
        self.mem_list[2] = 2

    def GetWays(self, number):
        if (number == 1) & (number == 2) & (number == 0):
            return number

        if self.mem_list[number] != 0:
            return self.mem_list[number]

        value = self.GetWays(number - 1) + self.GetWays(number - 2)

        self.mem_list[number] = value

        return value


if __name__ == '__main__':
    n = int(input())
    # n = 100

    s = Solution()

    res = s.GetWays(n)

    print(res)
