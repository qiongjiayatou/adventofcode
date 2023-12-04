# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 14:09:55 2021

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

gamma = []
epsilon = []

for i in range(len(content[0])):    
    count_zero = 0
    count_one = 0
        
    for line in content:
        num = get_number(list(line), i)
        if num == '0':
            count_zero += 1
        elif num == '1':
            count_one += 1
        # print(num)
    
    if count_zero > count_one:
        gamma.append('0')
        epsilon.append('1')
    else:
        gamma.append('1')
        epsilon.append('0')
        
    # print(len(content[0]), 'count_zero:', count_zero, 'count_one:', count_one, 'gamma:', gamma, 'epsilon:', epsilon)


gamma_dec = binary_to_decimal(gamma)
epsilon_dec = binary_to_decimal(epsilon)
power_consumption = gamma_dec*epsilon_dec
print(gamma_dec, epsilon_dec, power_consumption)


    

# print(binary_to_decimal(['0', '1', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0']))