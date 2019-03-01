# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 01:10:20 2019

@author: Sharvari
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        root = (x)**(0.5)
        return int(root)