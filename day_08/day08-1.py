DEBUG = False

class CamelMapNode:

    id = ''
    left = ''
    right = ''

    def __init__(self, n_id, left_n, right_n):
        self.left = left_n
        self.right = right_n

if DEBUG:
    file = open("day_08_input_test.txt", "r")
else:
    file = open("day_08_input.txt", "r")
original_data = file.read().strip().split("\n")
file.close()

camel_map_sack = dict()
rule_queue = []

first_line = True
for line in original_data:
    if first_line:
        for _c in line:
            rule_queue.append(_c)
        first_line = False
    
    if len(line) > 3:
        node_id = line[0:3]
        left_node = line[7:10]
        right_node = line[12:15]

        camel_map_sack[node_id] = CamelMapNode(node_id, left_node, right_node)

if DEBUG:
    for _k in camel_map_sack.keys():
        print(_k, end=' ')
        print(": " + str(camel_map_sack[_k].left) + ", " + str(camel_map_sack[_k].right))

curr_camel_map_node = 'AAA'
step_count = 0

while curr_camel_map_node != "ZZZ":
    if DEBUG:
        print("Current node:", curr_camel_map_node)

    if step_count % 10 == 0:
        print("Step", step_count)

    if rule_queue[0] == 'L':
        curr_camel_map_node = camel_map_sack[curr_camel_map_node].left
    elif rule_queue[0] == 'R':
        curr_camel_map_node = camel_map_sack[curr_camel_map_node].right

    rule_queue.append(rule_queue.pop(0))
    step_count += 1

print("Final count:", step_count)