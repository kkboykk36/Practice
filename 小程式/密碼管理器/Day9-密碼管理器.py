# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 16:13:25 2022

@author: AlenChang
"""

def add(name,account,pwd):
    with open('account.txt','r',encoding="utf-8") as file:
        line = file.read()
        print(line)
            # keys = list(line.keys())
            # values = list(line.values())
            
            # if keys == name:
            #     if values['account'] == account:
            #         msg = "已有帳號存在!"
            #         return msg
            #     else:
            #         account_key = {}
            #         account_value = {}
            #         account_value.setdefault('account',account)
            #         account_value.setdefault('password',pwd)
            #         account_key.setdefault(name,account_value)
            #         with open('account.txt','a',encoding="utf-8") as file:
            #             file.write(account_key)
            #         msg = "帳號新增成功!"
            #         return msg
# def query(name):
#     with open('account.txt','r',encoding="utf-8") as file:
#         for line in file:
#             keys = list(line.keys())
#             values = list(line.values())
#             if keys == name:
#                 if valaues['account'] == account:
    
    
print("歡迎使用密碼管理器!")
while True:
    choose = input("請輸入欲執行的動作(a新增 q查詢 e離開):")
    if choose.upper() == 'A':
        name = input("請輸入欲新增的應用程式名稱:")
        account = input("請輸入帳號:")
        pwd = input("請輸入密碼:")
        msg = add(name,account,pwd)
        print(msg)
    # elif choose.upper() == 'Q':
    #     name = input("請輸入欲查詢帳號名稱:")
    #     query(name)
    elif choose.upper() == 'E':
        break
    
print("謝謝使用!")        
        
