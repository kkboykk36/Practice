# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 15:48:58 2022

@author: AlenChang
"""

customer_spending ={
    "white":2000,
    "black":3000,
    "red": 12000,
    "geen":13000,
    "blue":8000
    }

for item in customer_spending:
    if customer_spending[item] < 10000:
        customer_spending[item] = '一般客戶'
    else:
        customer_spending[item] = 'VIP'
        

print(customer_spending)