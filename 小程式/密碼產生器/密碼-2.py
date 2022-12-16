# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 14:43:59 2022

@author: AlenChang
"""
import random

letters_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                 "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
                 "U", "V", "W", "X", "Y", "Z"]

letters_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j",
                 "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                 "u", "v", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "-", "+"]

def upper_ps(cnt):
    i = 1
    l_msg = ''
    a_msg = ''
    while i <= cnt:
        num = random.randint(0,len(letters_upper)-1)
        l_msg = letters_upper[num]
        a_msg = str(a_msg)+str(l_msg)
        i += 1
        
    return a_msg
        
def lower_ps(cnt):
    i = 1
    m_msg = ''
    b_msg = ''
    while i <= cnt:
        num = random.randint(0,len(letters_lower)-1)
        m_msg = letters_lower[num]
        b_msg = str(b_msg)+str(m_msg)
        i += 1
        
    return b_msg
    
def num_ps(cnt):
    i = 1
    n_msg = ''
    c_msg = ''
    while i <= cnt:
        num = random.randint(0,len(numbers)-1)
        n_msg = numbers[num]
        c_msg = str(c_msg)+str(n_msg)
        i += 1
    
    return c_msg
    
def symbols_num_ps(cnt):
    i = 1
    o_msg = ''
    d_msg = ''
    while i <= cnt:
        num = random.randint(0,len(symbols)-1)
        o_msg = symbols[num]
        d_msg = str(d_msg)+str(o_msg)
        i += 1
    
    return d_msg    

print("歡迎使用密碼產生器!")
let_upper = int(input("請問要幾個大寫字母?:\n"))
let_lower = int(input("請問要幾個小寫字母?:\n"))
num = int(input("請問要幾個數字?:\n"))
symbols_num = int(input("請問要幾個符號?:\n"))


msg1 = upper_ps(let_upper)
msg2 = lower_ps(let_lower)
msg3 = num_ps(num)
msg4 = symbols_num_ps(symbols_num)

# print(str(msg1)+str(msg2)+str(msg3)+str(msg4))

final_msg = str(msg1)+str(msg2)+str(msg3)+str(msg4)
pwd = list(final_msg)
random.shuffle(pwd)   #shuffle 是random將串列打亂的函式
new_pwd = ''

for x in pwd:
    new_pwd += x
    
print(new_pwd)












