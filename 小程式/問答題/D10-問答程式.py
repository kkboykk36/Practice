# -*- coding: utf-8 -*-
"""
Created on Mon Sep  5 18:04:46 2022

@author: AlenChang
"""

import json
import random

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
        
    def random_pick(self):
        new_question = []
        with open("questions.json","r",encoding="utf-8") as file:
            x = json.loads(file.read())
        num = random.randint(1,len(x))
        for z in range(num):
            cnt = random.randint(0, len(x)-1)
            new_question = new_question.append(x[cnt])
            
        return new_question
        
    
with open('questions.json','r',encoding='utf-8') as file:
    x = json.loads(file.read())
    
new_question=[]
for z in x:
    question = Question(z['description'], z['answer'])
    new_question = new_question.append(question)
questionPlay = Questions(new_question)
questionPlay.random_pick()
questionPlay.play()

    
