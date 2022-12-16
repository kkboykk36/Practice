# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 13:59:26 2022

@author: AlenChang
"""

scores_new = []
score = input("請輸入成績(並用,分開):")
new_score = score.split(',')


for num in new_score:
    num = int(num)
    scores_new.append(num)
    
    
max_num = 0
for num1 in scores_new:
    if num1 > max_num:
        max_num = num1
    else:
        continue

print("最大數為{}".format(max_num))