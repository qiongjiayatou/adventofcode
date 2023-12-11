import re
import math

file = open("../../files/2023-2.txt")
lines = file.read().split("\n")

res_sum = 0
for line in lines:
    red_sets = re.findall(r"(\d+)\s(?:red)", line)
    green_sets = re.findall(r"(\d+)\s(?:green)", line)
    blue_sets = re.findall(r"(\d+)\s(?:blue)", line)
    red_max = max(list(map(int, red_sets)))
    green_max = max(list(map(int, green_sets)))
    blue_max = max(list(map(int, blue_sets)))    
    
    res_sum += math.prod([red_max, green_max, blue_max])

print("Result: ", res_sum)
