# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 00:19:11 2019

@author: Sharvari
"""

class Solution(object):
    def isPalindrome(self, x):
        num = x
        rev = 0
        while(num>0):
            remainder = num%10
            rev = (rev*10)+remainder
            num = num/10
        if x<0:
            return False
        
        if rev==x:
            return True
        else:
            return False
        
s = Solution()
sol = s.isPalindrome(121)
print(sol)


#def isPalindrome(x):
#    num = x
#    rev = 0
#    while(num>0):
#        remainder = num%10
#        rev = (rev*10)+remainder
#        num = num/10
#    if x<0:
#        return False
#    if rev==x:
#        return True
#    else:
#        return False
#        
##s = Solution()
#x= 121
#print(isPalindrome(x))
