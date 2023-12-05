DEBUG = False

if DEBUG:
    file = open("day_04_input_test.txt", "r")
else:
    file = open("day_04_input.txt", "r")
original_data = file.read().strip().split("\n")
file.close()

total = 0

for line in original_data:
    count_wins = 0
    half_1, half_2 = line.split('|')

    winners = []
    scratch_nums = []

    for _t in half_1.split(":")[1].strip().split(' '):
        if _t.isdigit():
            winners.append(int(_t))

    for _t in half_2.strip().split(' '):
        if _t.isdigit():
            scratch_nums.append(int(_t))

    for _num in scratch_nums:
        if _num in winners:
            count_wins += 1
    
    if count_wins >= 1:
        total += 2 ** (count_wins-1)

print(total)