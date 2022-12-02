# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:58:52 2021

@author: Irini
"""

file = open('../files/1-2.txt')

lines = file.read().split('\n')
content = []
for line in lines:
    content.append(int(line))
    
i1 = 0
i2 = 1
i3 = 2

count = 0
first_sum = content[i1] + content[i2] + content[i3]
for i in content:
    if i3 == len(content)-1: 
        break
    
    i1 += 1
    i2 += 1
    i3 += 1
    
    next_sum = content[i1] + content[i2] + content[i3]
    
    if next_sum > first_sum:
        count += 1
    
    first_sum = next_sum
    
print(count)