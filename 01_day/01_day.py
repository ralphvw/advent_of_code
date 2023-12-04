file_path = 'data.txt'
sum = 0

with open(file_path, 'r') as f:
    lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        digits = ''.join([d for d in line if d.isdigit()])
        if len(digits) < 2:
            digits += digits
        else:
            digits = digits[0] + digits[-1]
        sum += int(digits)

print(sum) 