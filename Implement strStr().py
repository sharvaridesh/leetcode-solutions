# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 19:58:24 2019

@author: Sharvari
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle is None:
            return 0
        
        lenh=len(haystack)
        lenn=len(needle)
        
        if lenh<lenn:
            return -1
        
        for i in range(lenh-lenn+1):
            if haystack[i:i+lenn]==needle:
                return i
            
        return -1