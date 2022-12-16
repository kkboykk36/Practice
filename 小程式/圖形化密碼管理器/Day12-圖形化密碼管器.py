# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 11:08:40 2022

@author: AlenChang
"""

from tkinter import *
import tkinter.font as tkFont   #引入tk套件下的字形模組(tkinter.font)
from PIL import ImageTk     #引入插入圖片套件


window = Tk()  #創建視窗Tk物件
window.title("密碼管理器")   
window.geometry("300x600")
window.config(padx=30,pady=30)



img = ImageTk.PhotoImage(file='lock.png')
# window.iconphoto(True,img)   #第一個參數是指  是否要讓視窗沿用設定好的圖片
canvas = Canvas(width=224,height=225)    #圖片長 寬來設定畫布長寬
canvas.create_image(120,112,image=img)   #將圖片的中心點放在畫布中心點
canvas.grid(row=0,column=0,columnspan=2)

'''
帳號平台
'''
plantform = Label(text="帳號平台",font=('細明體',15))
plantform.grid(row=1,column=0)
plantform_entry = Entry()
plantform_entry.grid(pady=10,row=1,column=1)

'''
帳號
'''
weight = Label(text="帳號",font=('細明體',15))
weight.grid(row=2,column=0)
weight_entry = Entry()
weight_entry.grid(pady=10,row=2,column=1)

'''
密碼
'''
weight = Label(text="密碼",font=('細明體',15))
weight.grid(row=3,column=0)
weight_entry = Entry()
weight_entry.grid(pady=10,row=3,column=1)


'''
計算
'''
def click():
    w = int(weight_entry.get())
    h = int(height_entry.get()) * 0.01
    bmi = round(w/h**2,1)
    show['text']=('您的BMI:{}'.format(bmi))
    
button = Button(text='送出',font=("細明體", 10),command=click)
button.grid(row=4,column=0,columnspan=2)


window.mainloop()
               