DEBUG = False

color_list = ["red", "green", "blue"]

if DEBUG:
    file = open("day_02_input_test.txt", "r")
else:
    file = open("day_02_input.txt", "r")
original_data = file.read().strip().split("\n")

# each item likely will be a dict of R,G,B max num cubes
list_of_games = []

for line in original_data:
    temp_dict = {"red":[], "green":[], "blue":[]}

    for raw_cube_str in line.split(":")[1].split(';'):
        #print(raw_cube_str)
        for cube_count in raw_cube_str.strip().split(','):
            _count = int(cube_count.strip().split(' ')[0])
            color = cube_count.strip().split(' ')[1]

            temp_dict[color].append(_count)

    for color in color_list:
        if len(temp_dict) > 0:
            temp_dict[color] = max(temp_dict[color])
        else:
            temp_dict[color] = 0

    if DEBUG:    
        print(temp_dict)

    list_of_games.append(temp_dict)

total = 0

for game in list_of_games:
    power = 1

    for _color in color_list:
        power *= game[_color]

    total += power

print(total)

file.close()