# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 17:17:03 2022

@author: AlenChang
"""

class Question:
    def __init__(self,description,answer):
        self.description = description
        self.answer = answer
        
    def ask(self):
        ans = input(self.description)
        if ans == self.answer:
            return True
        else:
            return False
        

question = Question("1+1=?\n(a)2\n(b)3\n(c)4\n ", "a")
if question.ask():
    print("恭喜答對")
else:
    print("請加油") 