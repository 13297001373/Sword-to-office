'''
输入两个链表，找出它们的第一个公共结点。
'''
# -*- coding:utf-8 -*-
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        p1 = pHead1
        p2 = pHead2
        list1 = []
        while p1:
            list1.append(p1.val)
            p1 = p1.next
        while p2:
            if p2.val in list1:
                return p2
            else:
                p2 = p2.next

