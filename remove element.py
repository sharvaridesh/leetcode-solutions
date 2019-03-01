# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:32:23 2019

@author: Sharvari
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in nums[:]:
            if i==val:
                nums.remove(i)
                
        return len(nums)