# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 13:44:23 2022

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

def bmr(l_h,l_w,l_age,l_sex):
    if l_sex == "男":
        bmr = 66+(13.7*l_w)+5*l_h-6.8*l_age
    else:
        bmr = 655+(9.6*l_w)+1.8*l_h-4.7*l_age
        
    return bmr
    
def tdee(l_bmr,l_times):
    if l_times == '1':
        tdee = l_bmr*1.2
        print("計算總熱料消耗{}".format(tdee))
    elif l_times == '2':
        tdee = l_bmr*1.375
        print("計算總熱料消耗{}".format(tdee))
    elif l_times == '3':
        tdee = l_bmr*1.55
        print("計算總熱料消耗{}".format(tdee))
    elif l_times == '4':
        tdee = l_bmr*1.725
        print("計算總熱料消耗{}".format(tdee))
    else:
        tdee = l_bmr*1.9
        print("計算總熱料消耗{}".format(tdee))
    

print("歡迎使用綜合健康計算機!請選擇~")
print("(1)計算BMI")
print("(2)計算基礎代謝率(BMR)")
print("(3)計算總熱料消耗(TDEE)")

choose = input("請選擇要計算的項目(1 or 2 or 3):")
height = float(input("請輸入身高(公分):"))
wieght = float(input("請輸入體重(公斤):"))

if choose == '1':
    bmi(height,wieght)
elif choose == '2':
    age = int(input("請輸入年齡:"))
    sex = input("請輸入性別:")
    bmr = round(bmr(height,wieght,age,sex),2)
    print("基礎代謝率為{}".format(bmr))
else:
    sex = input("請輸入性別:")
    age = int(input("請輸入年齡:"))
    print("(1)久坐、幾乎沒運動")
    print("(2)每週低強度運動1~3天")
    print("(3)每週中強度運動3~5天")
    print("(4)每週高強度運動6~7天")
    print("(5)勞力密集工作或是每天高強度訓練")
    times = input("請輸入運動頻率(1 - 5):")
    bmr = bmr(height,wieght,age,sex)
    tdee(bmr,times)
    