# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 12:01:55 2022

@author: Irini
"""

file = open("../files/1.txt")
content = file.read().split("\n")
# print(content)

# for i in range(0, len(content)-2):
#     for n in range(1, len(content)-1):
#         # print(int(content[i]) + int(content[n]))
#         if int(content[i]) + int(content[n]) == 2020:
#             n1 = int(content[i])
#             n2 = int(content[n])
                
# print(n1 * n2)


for i in range(0, len(content)-3):
    for n in range(1, len(content)-2):
        for m in range(2, len(content)-1):
            if int(content[i]) + int(content[n]) + int(content[m]) == 2020:
                n1 = int(content[i])
                n2 = int(content[n])
                n3 = int(content[m])
                
print(n1 * n2 * n3)