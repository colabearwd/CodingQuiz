import random

class Solution:
    def __init__(self):
        self.step = 100000
        self.res = []

    def steps_needed(self, n):
        i, j = n, n

        def trackback(i, j, n, steps):
            if i < 0 or i > 2*n or j < 0 or j > 2*n:
                self.res.append(steps)
                return
            else:
                seek = random.randrange(1, 5)
                if seek == 1:
                    trackback(i+1, j, n, steps+1)
                elif seek == 2:
                    trackback(i-1, j, n, steps+1)
                elif seek == 3:
                    trackback(i, j+1, n, steps+1)
                else:
                    trackback(i, j-1, n, steps+1)

        for t in range(self.step):
            trackback(i, j, n, 0)
        expect = sum(self.res)/len(self.res)
        return expect


if __name__ == '__main__':
    y =Solution()
    x = y.steps_needed(3)
    print(x)
