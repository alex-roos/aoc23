def get_neighbors(row_index, col_index):
    neighbor_list = []

    # above row
    if row_index > 0:
        neighbor_list.append((row_index-1, col_index))
        if col_index > 0:
            neighbor_list.append((row_index-1, col_index-1))
        if col_index < LINE_WIDTH - 1:
            neighbor_list.append((row_index-1, col_index+1))
    # left and right
    if col_index > 0:
        neighbor_list.append((row_index, col_index-1))
    if col_index < LINE_WIDTH - 1:
        neighbor_list.append((row_index, col_index+1))
    # below row
    if row_index < COUNT_LINES - 1:
        neighbor_list.append((row_index + 1, col_index))
        if col_index > 0:
            neighbor_list.append((row_index + 1, col_index-1))
        if col_index < LINE_WIDTH - 1:
            neighbor_list.append((row_index + 1, col_index+1))

    return neighbor_list

DEBUG = False

if DEBUG:
    file = open("day_03_input_test.txt", "r")
else:
    file = open("day_03_input.txt", "r")
original_data = file.read().strip().split("\n")
file.close()

COUNT_LINES = len(original_data)
LINE_WIDTH = len(original_data[0])

values_dict = dict()
symbols_list = [[] for i in range(COUNT_LINES)]

value_guid = None

for line_num, _line in enumerate(original_data):
    # grab each value on the line of the strings along with all of the neighbors in grid
    # include a GUID with the value for the dictionary key tuple since there'll likely be value duplicates
    processing_number = False
    
    #print("Line", line_num)
    curr_neighbors = set()

    number_builder = []
    for col_idx, _token in enumerate(_line):
        
        if processing_number:

            if _token.isdigit():
                # another value to add to 
                number_builder.append(_token)
                curr_neighbors.update(get_neighbors(line_num, col_idx))

            else:
                processing_number = False

                values_dict[(int(''.join(number_builder)), value_guid)] = curr_neighbors

                if not _token == '.':
                    symbols_list[line_num].append((line_num, col_idx))                
        else:
            if _token.isdigit():
                number_builder = [_token]
                curr_neighbors = set()
                curr_neighbors.update(get_neighbors(line_num, col_idx))
                value_guid = (line_num, col_idx)
                processing_number = True
            elif not _token == '.':
                symbols_list[line_num].append((line_num, col_idx))
        
    if processing_number:
        values_dict[(int(''.join(number_builder)), value_guid)] = curr_neighbors

if DEBUG:
    for _val in values_dict.keys():
        _temp_list = list(values_dict[_val])
        _temp_list.sort()
        print(_val, "with neighbors", _temp_list)

parts_set = []
absolute_total = 0

print("Number of values:", len(values_dict.keys()))

total_symbols = 0
for i in symbols_list:
    total_symbols += len(i)

print("NUmber of symbols:", total_symbols)

for _val in values_dict.keys():
    row_of_value = _val[1][0]

    absolute_total += _val[0]

    #print("Working on val in row:", row_of_value)

    potential_adj_symbols = []
    for _s in symbols_list[row_of_value]:
        potential_adj_symbols.append(_s)
    if row_of_value > 0:
        for _s in symbols_list[row_of_value-1]:
            potential_adj_symbols.append(_s)
    if row_of_value < COUNT_LINES - 1:
        for _s in symbols_list[row_of_value+1]:
            potential_adj_symbols.append(_s)

    found_adj_symbol = False

    #print("Size of adj symbols:", len(potential_adj_symbols))

    for neighbor in values_dict[_val]:
        if neighbor in potential_adj_symbols:
            found_adj_symbol = True
            break

    if found_adj_symbol:
        parts_set.append(_val[0])
        if row_of_value == 94:
            print(_val[0])

# for _l in symbols_list:
#     print(_l)

print("Answer:", sum(parts_set))
print("All nums combined: ", absolute_total)