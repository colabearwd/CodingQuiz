'''
    爬楼梯，递归算法

'''


class Solution:


    def ClimbStairs(self, height):
        if (height == 0) or (height == 1) or (height == 2):
            return height

        return self.ClimbStairs(height - 1) + self.ClimbStairs(height - 2)


if __name__ == '__main__':

    height = int(input())

    s = Solution()
    res = s.ClimbStairs(height)
    print(res)
