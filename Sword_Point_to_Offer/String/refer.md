# 题目列表

## 01.ReplaceSpace
题目：
请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.
则经过替换之后的字符串为We%20Are%20Happy。

分析：依次遍历字符串的字符，拼接一个新的字符串。当是space时候，拼接"%20"；当是其他字符的时候，直接拼接



## 02.FirstAppearingOnce
题目：请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。当从该字符流中读出前六个字符“google"时，第一个只出现一次的字符是"l"。

分析：
首先设计一个类自带的字符串str和hash表（256位）。
然后InsertChar函数把每一个char加入到str，然后根据ord这个char的hash值，自增1
最后在FindAppeaingOnce函数中，遍历查看每一个char的hash表记录的值，第一个值位1的字符，或者返回#

