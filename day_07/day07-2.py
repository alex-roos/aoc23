DEBUG = True

if DEBUG:
    file = open("day_07_input_test.txt", "r")
else:
    file = open("day_07_input.txt", "r")
original_data = file.read().strip().split("\n")



file.close()