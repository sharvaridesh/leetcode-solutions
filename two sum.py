# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 22:19:05 2019

@author: Sharvari
"""

class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        for i,j in enumerate(nums):
            print(i)
            diff = (target - j)
            if diff in d:
                return [d[diff],i]
            else:
                d[j] = i
                
                
                
sol = Solution()
nums = [2, 7, 11, 15]
target = 17
s = sol.twoSum(nums,target)
print(s)

