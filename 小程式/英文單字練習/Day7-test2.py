# -*- coding: utf-8 -*-
"""
Created on Tue Aug 23 14:21:29 2022

@author: AlenChang
"""
import random
detail ={
    "小黑":{
        "age":23,
        "weight":65,
        "height":170},
    "小白":{
        "age":20,
        "weight":70,
        "height":175},
    "小蘭":{
        "age":22,
        "weight":50,
        "height":160}
    }

num = random.randint(0,2)
keys = list(detail.keys())
values = list(detail.values())
print(values)
print("選到的是{}".format(keys[num]))
values_dic = values[num]
print("年齡:{}".format(values_dic["age"]))
print("體重:{}".format(values_dic["weight"]))
print("身高:{}".format(values_dic["height"]))
