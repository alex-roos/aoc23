DEBUG = False

NUMBERS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

if DEBUG:
    file = open("day_01_input_test.txt", "r")
else:
    file = open("day_01_input.txt", "r")
original_data = file.read().strip().split("\n")

data = []

# extract 
for line in original_data:
    line_token_list = []

    # extract numbers as int's vs spelled out
    for _token_index, _token in enumerate(line):
        if _token.isdigit():
            line_token_list.append((int(_token), _token_index))

    _temp_line = line
   
    # check for each spelled-out number
    for _val_index, _num in enumerate(NUMBERS):

        _processing_line = _temp_line
        if DEBUG:
            print(_processing_line, "looking for", _num)

        offset_from_removed_strings = 0
        while _num in _processing_line:
            _idx = _processing_line.index(_num)

            # tuple of found spelled-out number, (number value, index in original string)
            line_token_list.append((_val_index, _idx + offset_from_removed_strings ))
            offset_from_removed_strings += len(_num) + _idx

            _processing_line = _processing_line[_idx+len(_num):]
        
        if DEBUG:
            print(line_token_list)
    
    # TODO - Rather than rebuild the string, create a list of numbers in the correct order
    # for _num_idx_to_add in numbers_to_add:
    #     _temp_line = _temp_line[:_num_idx_to_add[1]] + str(_num_idx_to_add[0]) + _temp_line[_num_idx_to_add[1]+len(_num):]

    line_token_list.sort(key=lambda x: x[1])
    data.append(line_token_list)

print("-"*25)
for _l in data:
    print(_l)

total = 0

# go through lists of parsed lines

for _l in data:
    print("Value:", _l[0][0], _l[len(_l) - 1][0])
    total += _l[0][0] * 10 + _l[len(_l) - 1][0]

print(total)

file.close()