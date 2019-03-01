# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 03:36:29 2019

@author: Sharvari
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        OPENING_BRACKETS = {"{", "[", "("}
        BRACKETS_MAP = {"]": "[", "}": "{", ")": "("}


        stack = []
        for bracket in s:
            if bracket in OPENING_BRACKETS:
                stack.append(bracket)
            elif not stack:
                return False        
            elif stack.pop() != BRACKETS_MAP[bracket]:
                return False       
        return not stack
