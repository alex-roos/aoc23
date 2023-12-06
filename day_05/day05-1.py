DEBUG = False

if DEBUG:
    file = open("day_05_input_test.txt", "r")
else:
    file = open("day_05_input.txt", "r")
original_data = file.read().strip().split("\n")
file.close()

seed_vals = []

# possible_states = {"seed-to-soil":0,
#                    "soil-to-fertilizer":1,
#                    "fertilizer-to-water":2,
#                    "water-to-light":3,
#                    "light-to-temperature":4,
#                    "temperature-to-humidity":5,
#                    "humidity-to-location":6
#                     }

almanac =       {"seed-to-soil":[],
                   "soil-to-fertilizer":[],
                   "fertilizer-to-water":[],
                   "water-to-light":[],
                   "light-to-temperature":[],
                   "temperature-to-humidity":[],
                   "humidity-to-location":[]
                    }

parse_state = ""

for line in original_data:
    is_header = False

    for _state in almanac.keys():
        if _state in line:
            is_header = True
            parse_state = _state

    if "seeds:" in line:
        for _t in line.split(':')[1].strip().split(' '):
            seed_vals.append(int(_t))
    elif is_header:
        pass
    elif len(line) > 1:
        src, dest, rng = line.strip().split(' ')
        almanac[parse_state].append([int(dest),int(src), int(rng)])

# first check if the mapping even exists or just one-to-one
# next figure out what range the mapping is in
# finally figure out what the offset is in that range

solutions = []

for seed in seed_vals:
    if DEBUG:
        print("-"*50)
        print("Seed starts at:", seed)
    for translation in almanac.keys():
        curr_mapping = almanac[translation]

        mapping_offset = 0
        
        for map_rule in curr_mapping:
            if seed < map_rule[0] + map_rule[2] and seed > map_rule[0]:
                mapping_offset = map_rule[1] - map_rule[0]
                print("RULE MATCHED:", map_rule)
        
        seed += mapping_offset

        if DEBUG:
            print(translation, seed)
    
    solutions.append(seed)

print("Solutions:", solutions)
print("MIN: ", min(solutions))