# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 03:06:53 2019

@author: Sharvari
"""

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        sum1 = (int(a,2)+int(b,2))
        return bin(sum1).replace("0b","")
