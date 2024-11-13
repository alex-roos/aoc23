DEBUG = True
VERBOSE = True
EXAMPLES = {"#.#.###": (1,1,3), ".#...#....###.": (1,1,3), ".#.###.#.######": (1,3,1,6), "####.#...#...":(4,1,1),
            "#....######..#####.": (1,6,5), ".###.##....#": (3,2,1)}

# for each size of permutation, lists possible indices permutations for each number of elements
PERMUTATION_SETS = dict()

if DEBUG:
    file = open("C:\\Users\\alexr\\dev\\aoc23\\day_12\\day_12_input_test.txt", "r")
else:
    file = open(".\\day_12_input.txt", "r")
original_data = file.read().strip().split("\n")
file.close()

def build_CRC(spring_single_row):
    dmg_grp_size_list = []
    in_dmg_group = False
    curr_grp_size = 0

    for token in spring_single_row:
        if in_dmg_group:
            if token == '.':
                dmg_grp_size_list.append(curr_grp_size)
                curr_grp_size = 0
                in_dmg_group = False
            elif token == '#':
                curr_grp_size += 1
        else:
            if token == '.':
                in_dmg_group = False
            elif token == '#':
                in_dmg_group = True
                curr_grp_size += 1

    if in_dmg_group:
        dmg_grp_size_list.append(curr_grp_size)

    return dmg_grp_size_list

# This method builds possible arrangements of broken springs in order (relative positions)
def build_permutations(count_unknowns):
    if count_unknowns not in PERMUTATION_SETS.keys():

        size_specific_permutations = {0: []} # prime dictionary with case where there are no broken springs
        # iterate thru each possible number of broken springs to fill each distinct unknown count
        for num_of_tokens in range(1, count_unknowns+1):
            # examples
            # Zero Unknowns
            # One Unknown
                # ['#']
                # ['.']
            # Two Unknowns
                # ['#', '#']
                # ['#', '.']
                # ['.', '#']
                # ['.', '.']
            # Three Unknowns
                # ['#', '#', '#']  - 0 periods
                # ['#', '#', '.']  - 1 period
                # ['#', '.', '#']  - 1 period
                # ['.', '#', '#']  - 1 period
                # ['#', '.', '.']  - 2 periods
                # ['.', '#', '.']  - 2 periods
                # ['.', '.', '#']  - 2 periods
                # ['.', '.', '.']  - 3 periods
            
            size_specific_permutations[num_of_tokens] = []

            start_idx = 0
            curr_list = []
            for i in range(num_of_tokens):
                curr_list.append(start_idx + i)

            size_specific_permutations[num_of_tokens].append(curr_list.copy())

            while curr_list[0] < count_unknowns - num_of_tokens:
                last_movable_idx = None
                check_for_movable = -1
                while last_movable_idx == None:
                    # starting at final index in list, look for furthest right that can move
                    if curr_list[check_for_movable] < count_unknowns + check_for_movable:
                        last_movable_idx = check_for_movable
                    elif abs(check_for_movable) > count_unknowns:
                        count_unknowns("ERROR: Looking too far back ")
                    else:
                        check_for_movable -= 1

                # now actually update the index and record the new permutation
                curr_list[last_movable_idx] += 1
                size_specific_permutations[num_of_tokens].append(curr_list)
                print("For token size", num_of_tokens, ":", size_specific_permutations[num_of_tokens])

        PERMUTATION_SETS[count_unknowns] = size_specific_permutations           

def build_posible_matches(corrupted_list, possible_breaks_list):
    indices_of_the_unknown = []
    for idx, token in enumerate(corrupted_list):
        if token == '?':
            indices_of_the_unknown.append(idx)
    
    if VERBOSE:
        print("Indices of the unknown:", indices_of_the_unknown)

    # build replacement combinations
    start_list = ['.'] * len(indices_of_the_unknown)

    combos_for_test = []

    for break_locs in possible_breaks_list:
        curr_break_list = start_list.copy()

        for idx in break_locs:
            curr_break_list[idx] = '#'

        combos_for_test.append(curr_break_list)


spring_row_list = []

for line in original_data:
    spring_condition, token_2 = line.strip().split(' ')
    continguous_damages = [int(x) for x in token_2.split(',')]

    spring_row_list.append([spring_condition, tuple(continguous_damages)])

if DEBUG:
    if VERBOSE:
        print("Input and broke list:", spring_row_list)

# naive method - 1) build ALL possible permutations of the missing question mark
#                2) determine which of those are valid matches (could potentially prune some paths with known inconsistencies)
        
for r in spring_row_list:
    if VERBOSE:
        print("String to match arrangements:", r[0])

    build_posible_matches(r[0])

# for record in EXAMPLES.keys():
#     curr_result = build_CRC(record)
#     #print("Comparing", curr_result, "to", EXAMPLES[record])
#     if tuple(curr_result) == EXAMPLES[record]:
#         print("Passed check.")
#     else:
#         print("Failed test.")