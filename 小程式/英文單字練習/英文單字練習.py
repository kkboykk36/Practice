# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 11:50:03 2022

@author: AlenChang
"""
import random

eng_dic = {
    "蘋果": "apple",
    "香蕉": "banana",
    "貓": "cat",
    "狗": "dog",
    "蛋": "egg",
    "食物": "food",
    "遊戲": "game",
    "手": "hand",
    "冰": "ice",
    "果醬": "jam",
    "國王": "king",
    "標籤": "label",
    "郵件": "mail",
    "脖子": "neck",
    "油": "oil",
    "豬": "pig",
    "皇后": "queen"
}

print("歡迎使用單字練習機~")
num = int(input("請問要練習的題數?"))
keys = list(eng_dic.keys())
values = list(eng_dic.values())



start = 1
err_cnt = 0
right_cnt = 0
while start <= num:
    cnt = random.randint(0,len(keys)-1)
    answer = str(input("請輸入" + str(keys[cnt]) + "答案?"))
    if answer != values[cnt]:
        print("答錯囉!正確是{}".format(values[cnt]))
        err_cnt += 1
        start += 1
    else:
        print("恭喜答對!")
        right_cnt +=1
        start += 1
    
print("共{}題,答對{}題,答錯{}題".format(num,right_cnt,err_cnt))
