import math

DEBUG = False

class CamelMapNode:

    id = ''
    left = ''
    right = ''

    def __init__(self, n_id, left_n, right_n):
        self.left = left_n
        self.right = right_n

def unreached_endpoints(curr_step_list):
    endpoints_remain = False

    for stepcount in curr_step_list:
        if stepcount == -1:
            endpoints_remain = True
            break

    return endpoints_remain

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

curr_camel_map_node_list = []
for _k in camel_map_sack.keys():
    if _k[2] == 'A':
        curr_camel_map_node_list.append(_k)

endpoint_stepcount_list = [-1] * len(curr_camel_map_node_list)
print("Total starting nodes:", len(curr_camel_map_node_list))

step_count = 0

# reached step_count 108000000 and climbing
# rather, we can determine the number of steps it takes to reach each concurrent endpoint
# and then find the ..... least common multiple... I think
while unreached_endpoints(endpoint_stepcount_list):
    if DEBUG:
        print("Current nodes:", curr_camel_map_node_list)

    if step_count % 1000000 == 0:
        print("Step", step_count)
        print(endpoint_stepcount_list)

    new_frontier = []
    for idx, node in enumerate(curr_camel_map_node_list):
        if endpoint_stepcount_list[idx] == -1 and node[2] == 'Z':
            endpoint_stepcount_list[idx] = step_count

        if rule_queue[0] == 'L':
            new_frontier.append(camel_map_sack[node].left)
        elif rule_queue[0] == 'R':
            new_frontier.append(camel_map_sack[node].right)

    curr_camel_map_node_list.clear()
    curr_camel_map_node_list = new_frontier.copy()
    rule_queue.append(rule_queue.pop(0))
    step_count += 1


print("Final count:", step_count)
print("LCM:", math.lcm(*endpoint_stepcount_list))