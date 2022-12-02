# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 19:38:09 2022

@author: Irini
"""

file = open('../files/1.txt')
elves = file.read().split("\n\n")

calories = []

for foods in elves:
    cal = 0
    for food in foods.split('\n'):
        cal += int(food)
        
    calories.append(cal)
    
max = 0;

for c in calories:
    if c > max:
        max = c

print(max)

calories.sort(reverse=True)  
threeMax = calories[:3]
print(sum(threeMax))
