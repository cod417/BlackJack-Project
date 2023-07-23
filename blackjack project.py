# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 14:06:54 2021

@author: lenovo
"""

# blackjack project
import random
def deck_card():

    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]   
        
    random_card = random.choice(cards)
        
    return random_card

answer = deck_card()
# print (answer)



def calculate_score(cards):
    
   if sum(cards) == 21 and len(cards) ==2:
   
    return 0

   if 11 in cards and sum(cards)>21:
    cards.remove(11)
    cards.append(1)
    return sum(cards)
user = int(input("enter no\n"))
score = calculate_score(user)
print (score)




