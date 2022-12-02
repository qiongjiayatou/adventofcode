# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 19:45:56 2021

@author: Irini
"""

file = open('../files/2-1.txt')
content = file.read().split('\n')
arr = []
for i in content:
    arr.append(i.split(' '))

horizontal = 0
depth = 0

for n in arr:
    if n[0] == 'forward':
        horizontal += int(n[1])
    elif n[0] == 'down':
        depth += int(n[1])
    elif n[0] == 'up':
        depth -= int(n[1])
    else:
        continue
    
print(horizontal, depth, horizontal*depth)