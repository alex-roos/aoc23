DEBUG = False

GAME_TRUTH = {"red": 12, "green": 13, "blue": 14}

if DEBUG:
    file = open("day_02_input_test.txt", "r")
else:
    file = open("day_02_input.txt", "r")
original_data = file.read().strip().split("\n")

# each item likely will be a dict of R,G,B max num cubes
list_of_games = []

for line in original_data:
    temp_dict = {"red":0, "green":0, "blue":0}

    for raw_cube_str in line.split(":")[1].split(';'):
        #print(raw_cube_str)
        for cube_count in raw_cube_str.strip().split(','):
            _count = int(cube_count.strip().split(' ')[0])
            color = cube_count.strip().split(' ')[1]

            if _count > temp_dict[color]:
                temp_dict[color] = _count

    if DEBUG:    
        print(temp_dict)

    list_of_games.append(temp_dict)

total = 0

for index, game in enumerate(list_of_games):
    found_conflict = False

    for _color in GAME_TRUTH.keys():
        if game[_color] > GAME_TRUTH[_color]:
            found_conflict = True
    
    if not found_conflict:
        total += index + 1

print(total)

file.close()