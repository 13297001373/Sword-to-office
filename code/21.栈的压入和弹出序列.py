'''
题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
'''
# -*- coding:utf-8 -*-
class Solution:
    def IsPopOrder(self, pushV, popV):
        if pushV[0] != popV[-1]:
            return False
        stack = []
        while popV:
            if pushV and pushV[-1] == popV[0]:
                pushV.pop()
                popV.pop(0)
            elif pushV:
                stack.append(pushV.pop())
            elif not pushV and stack:
                pushV+=[row for row in stack]
                stack = []
            else:
                return False
        return True
def test_function():
    solution = Solution()
    pushV = [1,2,3,4,5]
    popV = [4,3,5,1,2]
    print(solution.IsPopOrder(pushV,popV))

if __name__ == '__main__':
    test_function()


