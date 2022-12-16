# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 14:48:50 2022

@author: AlenChang
"""

sum_num = 0
for i in range(1,101):
    if i %2 ==0:
        sum_num += i
    else:
        continue
    
print("偶數和為:{}".format(sum_num))   
        