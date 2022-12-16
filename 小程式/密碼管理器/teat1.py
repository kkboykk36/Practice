# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 15:35:26 2022

@author: AlenChang
"""

tot = 0
with open("num.txt","r",encoding="utf-8") as file:
    for line in file:
        num = int(line)
        tot += num
        
print("總共是:{}".format(tot))
        