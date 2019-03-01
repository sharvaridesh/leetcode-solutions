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
    
    
    

#a="11"
#b="100"
#sum1 = (int(a,2)+int(b,2))
#print(sum1)
#binary1 = sum1
#decimal, i, n = 0, 0, 0
#while(sum1 != 0): 
#    dec = sum1 % 10
#    decimal = decimal + dec * pow(2, i) 
#    sum1 = sum1//10
#    i += 1
#print(decimal)