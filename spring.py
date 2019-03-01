# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 02:19:31 2019

@author: Sharvari
"""
str1='abbssd'
s = list(str1.strip())
print(s[0])
d = {}
count=0
for i,j in enumerate(s):
    if j not in d:
        d[j]=i
        count+=1
        print(d)
    elif j in d:
        i+=1
        continue
    
