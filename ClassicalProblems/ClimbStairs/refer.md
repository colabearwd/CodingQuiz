# 题目列表

## 爬楼梯问题
题目：有一座高度是n级台阶的楼梯，从下往上走，每跨一步只能向上1级或者2级台阶。求出一共有多少种走法。

分析：

    01递归算法
        当0，1，2时，返回相应的值
        当其他的值，返回第n-1和n-2的值
        
    02动态规划
        当0，1，2时，返回相应的值
        依次计算出每一个的结果
        
    03记录法-List
        当0，1，2时，返回相应的值
        查询n，在不在List中，如果在返回；如果不在，加入到List
        返回这次n的计算的结果
        
    04记录法-Dict
        当0，1，2时，返回相应的值
        查询n，在不在Dict中，如果在返回；如果不在，加入到List
        返回这次n的计算的结果


