# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:40:42 2022

@author: AlenChang
"""
# numlist =[]
# for i in range(3):
#     num = int(input("請輸入一整數:"))
#     i = num
#     numlist.append(i)
    
# max_num = 0
# for mx in range(numlist):
#     if mx > max_num:
#         max_num = mx
#     else:
#         continue
# print(max_num)



num1 = int(input("請輸入一整數:"))
num2 = int(input("請輸入一整數:"))
num3 = int(input("請輸入一整數:"))
    
def find_max(l_num1,l_num2,l_num3):
    if type(num1) != int or type(num2) != int or type(num3) != int:
        return "請輸入整數"
    
    if l_num1 > l_num2 and l_num1 > l_num3:
        return l_num1
    elif l_num2 > l_num1 and l_num2 > l_num3:
        return l_num2
    elif l_num3 > l_num1 and l_num3 > l_num2:
        return l_num3
    
def find_min(l_num1,l_num2,l_num3):
    if type(num1) != int or type(num2) != int or type(num3) != int:
        return "請輸入整數"
    
    if l_num1 < l_num2 and l_num1 < l_num3:
        return l_num1
    elif l_num2 < l_num1 and l_num2 < l_num3:
        return l_num2
    elif l_num3 < l_num1 and l_num3 < l_num2:
        return l_num3
        
def min_max(num1,num2,num3):
    max_num = find_max(num1,num2,num3)
    min_num = find_min(num1,num2,num3)
    
    return (max_num-min_num)
    

finial=min_max(num1,num2,num3)
print(finial)
    
    
    
    