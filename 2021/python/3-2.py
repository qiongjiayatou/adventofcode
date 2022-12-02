# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 20:17:57 2021

@author: Irini
"""

def get_number(list, index):
    return list[index]


def binary_to_decimal(list):
    num_dec = 0
        
    new_list = []
    for i in range(len(list),0,-1):
        new_list.append(i-1)
        # print(i-1)
        
    
    for i in range(len(list)):
        # print(list[i], new_list[i])
        num_dec += int(list[i]) * pow(2,new_list[i])
    print(num_dec)    
    return num_dec


file = open('../files/3.txt')
content = file.read().split('\n')

    
def rec(index, list, most_common = True):
    if len(list) == 1:
        return list[0]
    
    if index == len(list):
        index = 0
    
    count_zero = 0
    count_one = 0
    
    arr_zeros = []
    arr_ones = []
    
    arr = []
    for line in list:
        num = get_number(line, index)
        if num == '0':
            count_zero += 1
            arr_zeros.append(line)
        elif num == '1':
            count_one += 1
            arr_ones.append(line)
            
        if (count_one > count_zero and not most_common) or (
                count_one < count_zero and most_common) or (
                count_one == count_zero and not most_common):
            arr = arr_zeros               
        else:
            arr = arr_ones                 
            
    return rec(index+1, arr, most_common)
    
oxigen = binary_to_decimal(rec(0, content))
co2 = binary_to_decimal(rec(0, content, False))
life_support_rating = oxigen * co2


print(oxigen, co2, life_support_rating)