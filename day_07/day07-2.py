DEBUG = False

CARD_VALUES = {'A': 14,
               'K': 13,
               'Q': 12,
               'J': 1,
               'T': 10,
               '9':9,
               '8':8,
               '7':7,
               '6':6,
               '5':5,
               '4':4,
               '3':3,
               '2':2}

HAND_TYPES = {"Five of a kind": 6,
              "Four of a kind": 5,
              "Full house": 4,
              "Three of a kind": 3,
              "Two pair": 2,
              "One pair": 1,
              "High card": 0}

def determine_type(hand):
    card_counts = dict()
    for _c in CARD_VALUES.keys():
        card_counts[_c] = 0

    for _item in hand:
        card_counts[_item] += 1

    hand_counts = list(card_counts.values())
    hand_counts.sort()
    hand_counts.reverse()

    if DEBUG:
        print(hand_counts)

    if 'J' in hand:
        print("Things get crazy.")
        if card_counts['J'] == 5 or card_counts['J'] == 4:
            return "Five of a kind"
        elif card_counts['J'] == 3:
            if hand_counts[1] == 2:
                return "Five of a kind"
            else:
                return "Four of a kind"
        elif card_counts['J'] == 2:
            if hand_counts[0] == 3:
                return "Five of a kind"
            elif hand_counts[0] == 2 and hand_counts[1] == 2:
                return "Four of a kind"
            elif hand_counts[0] == 2 and hand_counts[1] == 1:
                return "Full house"
            else:
                return "Three of a kind"
        else:
            if hand_counts[0] == 4:
                return "Five of a kind"
            elif hand_counts[0] == 3:
                return "Four of a kind"
            elif hand_counts[0] == 2 and hand_counts[1] == 2:
                return "Full house"
            elif hand_counts[0] == 2 and hand_counts[1] == 1:
                return "Three of a kind"
            else:
                return "Two pair"

        
    else:
        if hand_counts[0] == 5:
            return "Five of a kind"
        elif hand_counts[0] == 4:
            return "Four of a kind"
        elif hand_counts[0] == 3:
            if hand_counts[1] == 2:
                return "Full house"
            else:
                return "Three of a kind"
        elif hand_counts[0] == 2 and hand_counts[1] == 2:
            return "Two pair"
        elif hand_counts[0] == 2:
            return "One pair"
        else:
            return "High card"

if DEBUG:
    file = open("day_07_input_test.txt", "r")
else:
    file = open("day_07_input.txt", "r")
original_data = file.read().strip().split("\n")
file.close()

hands_by_type = dict()
for num in range(7):
    hands_by_type[num] = []

for line in original_data:
    cards, bid = line.split(' ')
    bid = int(bid)

    card_list = list(cards)
    
    if DEBUG:
        print(card_list, "is", determine_type(card_list))

    _curr_values = []
    for _c in card_list:
        _curr_values.append(CARD_VALUES[_c])

    hands_by_type[HAND_TYPES[determine_type(card_list)]].append([_curr_values, bid])

if DEBUG:
    print('+'*100)
    print(hands_by_type)

final_order = []

for num in range(6,-1,-1):

    if len(hands_by_type[num]) > 1:
        tied_type = hands_by_type[num]
        tied_type.sort()
        tied_type.reverse()

        for _tie in tied_type:
            final_order.append(_tie[1])

    elif len(hands_by_type[num]) == 1:
        final_order.append(hands_by_type[num][0][1])

final_order.reverse()
print(final_order)

sum = 0
for i in range(len(final_order)):
    sum += final_order[i] * (i+1)

print(sum)