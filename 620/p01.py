'''
题目描述：合并两个有序列表
分析思路：
'''
import time


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        if l1.val <= l2.val:
            ret = l1
            ret.next = self.mergeTwoLists(self, l1.next, l2)
        else:
            ret = l2
            ret.next = self.mergeTwoLists(self, l1, l2.next)
        return ret


head1 = ListNode(2)
n1 = ListNode(3)
n2 = ListNode(4)
n3 = ListNode(5)
head1.next = n1
n1.next = n2
n2.next = n3

head2 = ListNode(3)
m1 = ListNode(5)
m2 = ListNode(7)

m3 = ListNode(9)
head2.next = m1
m1.next = m2
m2.next = m3

# while head1:
#     print(head1.val)
#     head1 = head1.next
# while head2:
#     print(head2.val)
#     head2 = head2.next

start = time.time()
res = Solution.mergeTwoLists(Solution, head1, head2)
end = time.time()
print(start - end)
while res:
    print(res.val)
    res = res.next
