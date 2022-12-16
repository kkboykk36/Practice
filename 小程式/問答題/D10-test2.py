# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 17:21:02 2022

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

class Questions:
    def __init__(self,questions,score):
        self.questions = questions
        self.score = score
        
    def play(self):
        num = 0
        for i in self.questions:
            if i.ask():
                print("恭喜答對")
                num += 1
            else:
                print("請加油，答案是{}".format(i.answer))
        
        print("共答對{}".format(num))
    

question1 = Question("1+1=?\n(a)2\n(b)3\n(c)4\n ", "a")
question2 = Question("1+3=?\n(a)2\n(b)3\n(c)4\n ", "c")
question3 = Question("1+5=?\n(a)2\n(b)6\n(c)4\n ", "b")
questions = [question1,question2,question3]
questionPlay = Questions(questions,0)
questionPlay.play()

