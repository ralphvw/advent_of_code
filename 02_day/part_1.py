import re

file_path = 'data.txt'


total_red = 12
total_green = 13
total_blue = 14

invalid_games = set()
total_games = 0

with open(file_path, 'r') as f:
    lines = f.readlines()
    
for line in lines:
    print(f'Line: {line}')
    red = 0
    green = 0
    blue = 0
    game_number, game_data = line.split(':')
    game_number = game_number.split()[-1]
    total_games += int(game_number)
    game_data = re.split(r',|;', game_data)
    print(f'Game Data: {game_data}')
    for data in game_data:
        number, color = data.split()
        print(f'Color: {color}, Number: {number}, Data: {data}')
        if color == 'red':
            if int(number) > total_red:
                invalid_games.add(int(game_number))
        if color == 'blue':
            if int(number) > total_blue:
                invalid_games.add(int(game_number))
        if color == 'green':
            if int(number) > total_green:
                invalid_games.add(int(game_number))


print(invalid_games) 
sum = total_games - sum(invalid_games)

print(sum)