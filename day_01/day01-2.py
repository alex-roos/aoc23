DEBUG = True

if DEBUG:
    file = open("day_01_input_test.txt", "r")
else:
    file = open("day_01_input.txt", "r")
data = file.read().strip().split("\n")



file.close()