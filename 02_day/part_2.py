import re

file_path = 'data.txt'
sum = 0

with open(file_path, 'r') as f:
    lines = f.readlines()
    
for line in lines:
    max_red = 0
    max_green = 0
    max_blue = 0
    game_number, game_data = line.split(':')
    game_number = game_number.split()[-1]
    game_data = re.split(r',|;', game_data)
    for data in game_data:
        number, color = data.split()
        if color == 'red':
            max_red = max(int(number), max_red)
        if color == 'blue':
            max_blue = max(int(number), max_blue)
        if color == 'green':
            max_green = max(int(number), max_green)
    power = max_red * max_green * max_blue
    sum += power

print(sum)
