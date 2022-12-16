# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 10:01:42 2022

@author: AlenChang
"""

import random

answer = random.randint(1, 100)
cnt = 5
start = 1
print("歡迎來到終極密碼!!!")
print("請小心猜...你只有5次機會!!")
while start <= cnt:
    print("第{}次".format(start))
    num = input("請猜一個正整數:\n")
    if num.isdigit():    #判斷字串是否為數值函式
        num = int(num)
    else:
        print("請輸入大於0之整數")
        start += 1
        continue
    
    
    if num == answer:
        print("恭喜猜對!")
        start += 1
        sucess = 'Y'
        break
    else:
        if num < answer:
            print("猜錯囉!，再大一點!")
            start += 1
            sucess = 'N'
        else:
            print("猜錯囉!，再小一點!")
            start += 1
            sucess = 'N'

if start > cnt and sucess == 'N':
    print("你輸了,答案是{}".format(answer))