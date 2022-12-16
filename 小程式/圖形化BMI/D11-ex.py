# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 00:55:15 2022

@author: User
"""

#tkinter 模組(套件)  GUI程式 圖形化介面
#創建視窗，標籤
#改變設定，創建按鈕，創建輸入框

from tkinter import *
import tkinter.font as tkFont   #引入tk套件下的字形模組(tkinter.font)

window = Tk()  #創建視窗Tk物件
"""
視窗內的程式活動須寫在視窗創建與視窗關閉之間
"""
window.title("邦特自己人")   #利用title method 來設定程式標題
window.geometry("300x300") #利用geometry method 來設定畫面大小(長x寬)
window.maxsize(width='400',height='400') #利用maxsize 來限制畫面最大尺寸  反之minsize就是最小尺寸
# window.resizable(False,False)    #當視窗創建大小後即固定尺寸(長(布林值),寬(布林值)  False(不可改變),True(可改變)


my_label = Label(text='Hello World!',font=("細明體", 30))  #創建文字標籤 #font (字形,大小)
my_label.pack(side='top')     #設定文字標籤位置/上top 左left 右right 下bottom。若參數空白則預設在上方(top)
# tkFont.families()    #tkFont套件下的families method會回傳所有字體


"""
兩種方式更改label內容及字體大小
1.指定關鍵字
2.使用config method
"""
#1.
# my_label['text']="Yes!"   #直接指定關鍵字
# my_label['font']=("細明體",20)  #直接指定關鍵字

#2.
# my_label.config(text='Yes World!',font=("細明體", 50))

"""
創建按鈕
"""
def click():
    # my_label['text'] = "Change!"
    my_label['text'] = my_entry.get()  #將輸入框的文字回傳出來
my_button = Button(text='送出',font=("標楷體", 15),command=click) #要讓按鈕執行的動作要加command參數，參數右邊要是函示
my_button.pack(side='top')     

"""
創建輸入框
"""
my_entry = Entry()
my_entry.pack(side='top')  
# my_entry.get()  #將輸入框的文字回傳出來

"""
數值輸入框spinbox
"""
# def use_spinbox():
#     print(my_spinbox.get())
    
# my_spinbox = Spinbox(
#                      to=100,
#                      width=20,
#                      command=use_spinbox)
# my_spinbox.pack(side='top')  


"""
拉桿scale
"""
# def use_scale(value):
#     print(value)
# my_scale = Scale(from =0,
#                  to=100,
#                  width=20,
#                  command=use_scale)
# my_scale.pack(side='top')  


"""

"""

window.mainloop()  #爭測試窗發生的事件