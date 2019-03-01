# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 01:24:45 2019

@author: Sharvari
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (abs(x)>pow(2,31)):
            return 0
        else:
            if x<0:
                num=x*(-1)
            else:
                num=x
            rev=0
            rev1=0
            while(num>0):
                remainder=num%10
                rev=(rev*10)+remainder
                num=num/10
        
            if rev>pow(2,31):
                return 0
        
            if(x<0):
                return rev*-1
            else:
                return rev
                