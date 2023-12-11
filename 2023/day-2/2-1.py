import re

file = open("../files/2.txt")
lines = file.read().split("\n")

def check(num, color):
    MAX_RED = 12
    MAX_GREEN = 13
    MAX_BLUE = 14

    if (color == "red" and int(num) > MAX_RED 
        or color == "green" and int(num) > MAX_GREEN
        or color == "blue" and int(num) > MAX_BLUE):
        return False
    else:
        return True

game_sum = 0
for line in lines:
    game_number = re.search(r"Game (\d+):", line)    
    game_sets = re.findall(r"(\d+\s(?:red|green|blue))", line)    

    is_valid = True
    for set in game_sets:
        m = re.search(r"(\d+)\s(red|green|blue)", set)        
        if not check(m.group(1), m.group(2)):
            is_valid = False
            break
    
    if is_valid:
        game_sum = game_sum + int(game_number.group(1))

    
print("Result: ", game_sum)    
        

    
    