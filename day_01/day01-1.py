DEBUG = False

if DEBUG:
    file = open("day_01_input_test.txt", "r")
else:
    file = open("day_01_input.txt", "r")
data = file.read().strip().split("\n")

token_list = []

for line in data:
    _temp = []
    for _t in line:
        if _t.isdigit():
            _temp.append(int(_t))

    token_list.append(_temp)

total = 0

for _l in token_list:
    total += _l[0] * 10 + _l[len(_l) - 1]

print(total)

file.close()