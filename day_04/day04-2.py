DEBUG = False

if DEBUG:
    file = open("day_04_input_test.txt", "r")
else:
    file = open("day_04_input.txt", "r")
original_data = file.read().strip().split("\n")
file.close()

# idx 0 is winning nums, idx 1 is scratched nums
card_list = []

for line in original_data:
    half_1, half_2 = line.split('|')

    winners = []
    scratch_nums = []

    for _t in half_1.split(":")[1].strip().split(' '):
        if _t.isdigit():
            winners.append(int(_t))

    for _t in half_2.strip().split(' '):
        if _t.isdigit():
            scratch_nums.append(int(_t))
    
    card_list.append([winners, scratch_nums])

# [0] = num wins, [1] num of copies
card_wins = [1 for x in range(len(card_list))]

for card_index, card_set in enumerate(card_list):
    multiplier = card_wins[card_index]
    count_wins = 0
    for _num in card_set[1]:
        if _num in card_set[0]:
            count_wins += 1

    for _copy in range(multiplier):
        for knock_on_idx in range(1,count_wins+1):
            card_wins[card_index + knock_on_idx] += 1 

print(card_wins)    
print(sum(card_wins))