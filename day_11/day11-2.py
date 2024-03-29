DEBUG = False
VERBOSE = False

EXPANSION = 1000000 - 1
EMPTY_SPACE_ROWS = []
EMPTY_SPACE_COLS = []

def create_combinations(size):
    combos = []
    for i in range(size):
        for j in range(i+1, size):
            combos.append((i,j))

    return combos

def calc_galactic_distance(galaxy_1, galaxy_2):
    horizontal_diff = abs(galaxy_1[1] - galaxy_2[1])
    vertical_diff = abs(galaxy_1[0] - galaxy_2[0]) 

    extra_columns = 0
    extra_rows = 0

    for i in range(min(galaxy_1[0], galaxy_2[0]), max(galaxy_1[0], galaxy_2[0])):
        if i in EMPTY_SPACE_ROWS:
            extra_rows += 1

    for i in range(min(galaxy_1[1], galaxy_2[1]), max(galaxy_1[1], galaxy_2[1])):
        if i in EMPTY_SPACE_COLS:
            extra_columns += 1

    return horizontal_diff + (extra_columns * EXPANSION) + vertical_diff + (extra_rows * EXPANSION)

if DEBUG:
    file = open("day_11_input_test.txt", "r")
else:
    file = open("day_11_input.txt", "r")
original_data = file.read().strip().split("\n")

file.close()

galaxy_list = []
column_contents = [[] for x in range(len(original_data[0]))]

# parse the input file
for row, line in enumerate(original_data):
    all_space = True
    for _col, _char in enumerate(line):
        column_contents[_col].append(_char)
        if _char == '#':
            galaxy_list.append((row, _col))
            all_space = False

    if all_space:
        EMPTY_SPACE_ROWS.append(row)

for col_id, full_column in enumerate(column_contents):
    if not '#' in full_column:
        EMPTY_SPACE_COLS.append(col_id)

if VERBOSE:
    print(galaxy_list)

total_dist = 0

for combo in create_combinations(len(galaxy_list)):
    g_1 = galaxy_list[combo[0]]
    g_2 = galaxy_list[combo[1]]
    if VERBOSE:
        print("G_1", g_1, "to", "G_2", g_2, end=': ')

    curr_dist = calc_galactic_distance(g_1, g_2)
    total_dist += curr_dist

    if VERBOSE:
        print(curr_dist)  

# too high: 483845200392
# too low:      82000292
# too low:      82000210
print("Total Distance:", total_dist)
print(EMPTY_SPACE_COLS)