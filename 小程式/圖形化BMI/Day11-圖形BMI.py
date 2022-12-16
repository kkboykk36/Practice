# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 11:08:40 2022

@author: AlenChang
"""

from tkinter import *
import tkinter.font as tkFont   #引入tk套件下的字形模組(tkinter.font)

window = Tk()  #創建視窗Tk物件
window.title("BMI計算器")   
window.geometry("300x300")
window.config(padx=30,pady=30)
'''
身高
'''
height = Label(text="身高",font=('細明體',15))
height.grid(row=0,column=0)
height_entry = Entry()
height_entry.grid(pady=10,row=0,column=1)
height_unit = Label(text="公分",font=('細明體',15))
height_unit.grid(row=0,column=2)

'''
體重
'''
weight = Label(text="體重",font=('細明體',15))
weight.grid(row=1,column=0)
weight_entry = Entry()
weight_entry.grid(pady=10,row=1,column=1)
weight_unit = Label(text="公斤",font=('細明體',15))
weight_unit.grid(row=1,column=2)

'''
顯示
'''
show = Label(text='您的BMI:',font=('細明體',10))
show.grid(row=2,column=1)
'''
計算
'''
def click():
    w = int(weight_entry.get())
    h = int(height_entry.get()) * 0.01
    bmi = round(w/h**2,1)
    show['text']=('您的BMI:{}'.format(bmi))
    
button = Button(text='計算',font=("細明體", 10),command=click)
button.grid(row=3,column=1)

window.mainloop()
               