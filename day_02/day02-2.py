DEBUG = False

if DEBUG:
    file = open("day_02_input_test.txt", "r")
else:
    file = open("day_02_input.txt", "r")
original_data = file.read().strip().split("\n")



file.close()