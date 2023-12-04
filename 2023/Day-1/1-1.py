
file = open('input.txt')
lines = file.read().split("\n")

collection = []
for line in lines:        
    numbers = []
    for letter in line:
        if letter.isdigit():            
            numbers.append(letter)        
        
    num = numbers[0] + str(numbers[len(numbers)-1])
    collection.append(num)

result = 0
for n in collection:
    result = result + int(n)

print("Result: ", result)

    
  
    
            