# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# A for Rock, B for Paper, and C for Scissors

def play(opponent, me):
    score = 0
    if opponent == 'A' and me == 'X' or opponent == 'B' and me == 'Y' or opponent == 'C' and me == 'Z':
        score += 3
    elif opponent == 'A' and me == 'Y' or opponent == 'B' and me == 'Z' or opponent == 'C' and me == 'X':
        score += 6
    
    if me == "X":
        score += 1
    elif me == "Y":
        score += 2
    elif me == "Z":
        score += 3
        
    return score

def adjust_game(opponent, me):
    if me == "X":
        if opponent == "A":
            return "Z"
        elif opponent == "B":
            return "X"
        elif opponent == "C":
            return "Y"
    elif me == "Y":
        if opponent == "A":
            return "X"
        elif opponent == "B":
            return "Y"
        elif opponent == "C":
            return "Z"
    elif me == "Z":
        if opponent == "A":
            return "Y"
        elif opponent == "B":
            return "Z"
        elif opponent == "C":
            return "X"
    

file = open('../files/2.txt')
content = file.read().split("\n")

new_list = []
for i in content:
    new_list.append(i)
    # print(i)
    
    
res = 0
for i in new_list:
    guide = i.split(" ")
    me = adjust_game(guide[0], guide[1])
    res += play(guide[0], me)
    
print(res)