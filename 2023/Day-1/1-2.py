file = open('input.txt')
lines = file.read().split("\n")

def replaceStrToNumber(str):
    return str.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9")

collection = []

for line in lines:        
    line = replaceStrToNumber(line)
    numbers = []
    for letter in line:
        if letter.isdigit():            
            numbers.append(letter)        
            
    print(line)
    print(numbers)
    num = numbers[0] + str(numbers[len(numbers)-1])
    print(num)
    collection.append(num)

result = 0
for n in collection:
    result = result + int(n)

print("Result: ", result)
