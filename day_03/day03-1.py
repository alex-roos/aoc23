DEBUG = True

if DEBUG:
    file = open("day_03_input_test.txt", "r")
else:
    file = open("day_03_input.txt", "r")
original_data = file.read().strip().split("\n")


for _line in original_data:
    # grab each value on the line of the strings along with all of the neighbors in grid
    # include a GUID with the value for the dictionary key tuple since there'll likely be value duplicates

    pass

file.close()