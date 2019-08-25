'''
    爬楼梯，备忘录法
'''


class Solution:
    def __init__(self):
        self.mem_dict = {}
        self.mem_dict['0'] = 0
        self.mem_dict['1'] = 1
        self.mem_dict['2'] = 2

    def GetWays(self, number):
        if (number == 1) & (number == 2) & (number == 0):
            return number

        if str(number) in self.mem_dict.keys():
            return self.mem_dict[str(number)]

        value = self.GetWays(number - 1) + self.GetWays(number - 2)

        self.mem_dict[str(number)] = value

        return value


if __name__ == '__main__':
    # n = int(input())
    n = 10

    s = Solution()

    res = s.GetWays(n)

    print(res)

    print(s.mem_dict)
