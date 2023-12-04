# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 19:07:07 2021

@author: Irini
"""

file = open('../files/1-1.txt')
content = file.read().split('\n')
first = content[0]
content.pop(0)
print(first)
count = 0

for line in content:
    if int(line) > int(first):
        count += 1
    first = int(line)

print(count)
