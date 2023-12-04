import re

words_to_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

file_path = 'data.txt'
sum = 0

with open(file_path, 'r') as f:
    lines = f.readlines()
    
for line in lines:
    print(f'Line: {line}')
    left = 0
    digits = '0'
    while left < len(line):
        if line[left].isdigit():
            digits += line[left]
        if left < len(line) - 1:
            right = left + 1
            while right < len(line):
                input = line[left : right + 1]
                if input in words_to_digits:
                    digits+= words_to_digits[input]
                right += 1
        print(f'Digits: {digits}')
        if len(digits) < 2:
            final = 0
        else:
            final = digits[1] + digits[-1]
        print(f'Final: {final}')
        left += 1
    sum += int(final)  
print(sum)