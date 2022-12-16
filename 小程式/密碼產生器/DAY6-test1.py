# -*- coding: utf-8 -*-
"""
Created on Tue Aug 16 11:15:37 2022

@author: AlenChang
"""

def bmi(l_h,l_w):
    l_h *= 0.01
    bmi = l_w/l_h**2
    bmi = round(bmi,1)
    if bmi < 18.5:
        print("{}體重過輕".format(bmi))
    elif 18.5 <= bmi and bmi < 24:
        print("{}體重標準".format(bmi))
    elif 24 <= bmi and bmi < 27:
        print("{}體重過重".format(bmi))
    elif 27 <= bmi and bmi < 30:
        print("{}輕度肥胖".format(bmi))
    elif 27 <= bmi and bmi < 30:
        print("{}輕度肥胖".format(bmi))
    elif 30 <= bmi and bmi < 35:
        print("{}輕度肥胖".format(bmi))
    else:
        print("{}重度肥胖".format(bmi))

again = 'Y'

while again == 'Y':
    height = float(input("請輸入身高(公分):"))
    wieght = float(input("請輸入體重(公斤):"))
    bmi(height,wieght)
    again = input("是否還要繼續只使用?(y or n)").upper()
    if again != 'Y':
        again = 'N'


print("謝謝使用!")

