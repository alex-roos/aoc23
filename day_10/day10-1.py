DEBUG = False
VERBOSE = False

class PipeNode:

    connected_pipe_locations = set()
    loc = (-1, -1)
    dist_from_start = None
    symbol = ' '

    def __init__(self, row, col, sym = '.'):
        self.connected_pipe_locations = set()
        self.loc = (row, col)
        self.dist_from_start = None
        self.symbol = sym

    def add_connection(self, _in):
        self.connected_pipe_locations.add(_in)
    
    def update_symbol(self, _sym):
        self.symbol = _sym

def update_connections(start_node, new_connect_locations):
    for _connection_loc in new_connect_locations:
        if _connection_loc[0] >= 0 and _connection_loc[0] <= 139 and _connection_loc[1] >= 0 and _connection_loc[1] <= 139:
            PIPE_DICT[start_node].add_connection(_connection_loc)

            PIPE_DICT[_connection_loc].add_connection(start_node)

class PipeTraverser:

    current_node_loc = None
    depth = 0

    def __init__(self, _start_node, _init_depth=1):
        self.current_node_loc = _start_node
        self.depth = _init_depth

if DEBUG:
    #file = open("C:\\Users\\alexr\\git\\aoc23\\day_10\\day_10_input_test.txt", "r")
    file = open("C:\\Users\\alexr\\dev\\aoc23\\day_10\\day_10_input_test.txt", "r")
else:
    file = open("C:\\Users\\alexr\\dev\\aoc23\\day_10\\day_10_input.txt", "r")
original_data = file.read().strip().split("\n")
file.close()

count_rows = len(original_data)
count_col = len(original_data[0])

PIPE_DICT = dict()

for row_num, line in enumerate(original_data):
    for col_num, _curr_token in enumerate(line):
        PIPE_DICT[(row_num, col_num)] = PipeNode(row_num, col_num, _curr_token)

curr_row = 0
for line in original_data:
    if curr_row == 0:
        below_top_row = False
    else:
        below_top_row = True
    if curr_row == len(original_data) - 1:
        above_bottom_row = False
    else:
        above_bottom_row = True

    for _col, _token in enumerate(line):
        if _col == 0:
            right_of_left_edge = False
        else:
            right_of_left_edge = True

        if _col == len(line) - 1:
            left_of_right_edge = False
        else:
            left_of_right_edge = True

        # ['|', '-', 'L', 'J', '7', 'F']
        connections_to_add = []
        if _token == '|':
            # above and below
            if below_top_row and PIPE_DICT[(curr_row - 1, _col)].symbol in ['|', '7', 'F', 'S']:
                connections_to_add.append((curr_row - 1, _col))
            if above_bottom_row and PIPE_DICT[(curr_row + 1, _col)].symbol in ['|', 'L', 'J', 'S']:
                connections_to_add.append((curr_row + 1, _col))
        elif _token == '-':
            # left and right
            if right_of_left_edge and PIPE_DICT[(curr_row, _col -1)].symbol in ['-', 'L','F', 'S']:
                connections_to_add.append((curr_row, _col - 1))
            if left_of_right_edge and PIPE_DICT[(curr_row, _col + 1)].symbol in ['-', 'J', '7', 'S']:
                connections_to_add.append((curr_row, _col + 1))
        elif _token == 'L':
            # above and right
            if below_top_row and PIPE_DICT[(curr_row - 1, _col)].symbol in ['|', '7', 'F', 'S']:
                connections_to_add.append((curr_row - 1, _col))
            if left_of_right_edge and PIPE_DICT[((curr_row, _col + 1))].symbol in ['-', 'J', '7', 'S']:
                connections_to_add.append((curr_row, _col + 1))
        elif _token == 'J':
            # above and left
            if below_top_row and PIPE_DICT[(curr_row - 1, _col)].symbol in ['|', '7', 'F', 'S']:
                connections_to_add.append((curr_row - 1, _col))
            if right_of_left_edge and PIPE_DICT[(curr_row, _col -1)].symbol in ['-', 'L','F', 'S']:
                connections_to_add.append((curr_row, _col - 1))
        elif _token == '7': 
            # below and left
            if above_bottom_row and PIPE_DICT[(curr_row + 1, _col)].symbol in ['|', 'L', 'J', 'S']:
                connections_to_add.append((curr_row + 1, _col))
            if right_of_left_edge and PIPE_DICT[(curr_row, _col -1)].symbol in ['-', 'L','F', 'S']:
                connections_to_add.append((curr_row, _col - 1))
        elif _token == 'F':
            # below and right
            if above_bottom_row and PIPE_DICT[(curr_row + 1, _col)].symbol in ['|', 'L', 'J', 'S']:
                connections_to_add.append((curr_row + 1, _col))
            if left_of_right_edge and PIPE_DICT[((curr_row, _col + 1))].symbol in ['-', 'J', '7', 'S']:
                connections_to_add.append((curr_row, _col + 1))
        elif _token == 'S':
            start = (curr_row, _col)
            PIPE_DICT[start].dist_from_start = 0

        update_connections((curr_row, _col), connections_to_add)    

    curr_row += 1

if DEBUG:
    node_frontier = list(PIPE_DICT[start].connected_pipe_locations)
    left_path_traverser = PipeTraverser(node_frontier[0])
    right_path_traverser = PipeTraverser(node_frontier[1])
else:
    start_path_1, start_path_2 = PIPE_DICT[start].connected_pipe_locations
    if PIPE_DICT[start_path_1].loc[1] < PIPE_DICT[start_path_2].loc[1]:
        left_path_traverser = PipeTraverser(start_path_1)
        right_path_traverser = PipeTraverser(start_path_2)
    else:
        left_path_traverser = PipeTraverser(start_path_2)
        right_path_traverser = PipeTraverser(start_path_1)

    traversers = [left_path_traverser, right_path_traverser]

final_paths = []
for i in range(140):
    final_paths.append(['.']*140)

left_terminated = False
right_terminated = False

final_paths[start[0]][start[1]] = PIPE_DICT[start].symbol

while (not left_terminated or not right_terminated):
    if VERBOSE:
        print("Left depth:", left_path_traverser.depth)
        print("Right depth:", right_path_traverser.depth, "at node", right_path_traverser.current_node_loc, PIPE_DICT[right_path_traverser.current_node_loc].symbol)

    path_side = "left"
    for _curr_traverser in traversers:
        # updaate the distance for the node actually visited
        PIPE_DICT[_curr_traverser.current_node_loc].dist_from_start = _curr_traverser.depth

        _curr_frontier = PIPE_DICT[_curr_traverser.current_node_loc].connected_pipe_locations
        curr_next_node_loc = None

        # look through connected nodes, see which does not have a distance of none
        has_unvisited_node = False
        for _next_frontier_node_loc in _curr_frontier:
            if VERBOSE and path_side == "right":
                print(_next_frontier_node_loc, ":", PIPE_DICT[_next_frontier_node_loc].symbol, "has dist", PIPE_DICT[_next_frontier_node_loc].dist_from_start)
            if PIPE_DICT[_next_frontier_node_loc].dist_from_start == None:
                has_unvisited_node = True
                next_node_loc = _next_frontier_node_loc

        if has_unvisited_node:
            _curr_traverser.depth += 1
            _curr_traverser.current_node_loc = next_node_loc 

            final_paths[next_node_loc[0]][next_node_loc[1]] = PIPE_DICT[next_node_loc].symbol
        else:
            if path_side == "left":
                left_terminated = True
            elif path_side == "right":
                right_terminated = True

            if VERBOSE:
                print("End of the", path_side, "line.")

        path_side = "right"

print(left_path_traverser.depth)
print(right_path_traverser.depth)

write_file = open("C:\\Users\\alexr\\dev\\aoc23\\day_10\\debug_output.txt", "w")
for row in final_paths:
    temp_str = ""
    for _i in row:
        temp_str += _i

    write_file.write(temp_str)
    write_file.write('\n')

write_file.close()

# manual count for part 2 via output file, 247 is too low

# to find outer tiles
  # check if the tile is a '.', that means it is not part of the loop
  # check if the '.' is either
        # condition 1)  on the top row, bottow row, leftmost col, rightmost col -> if so, change '.' to 'O'
        # condition 2) touching a 'O' tile [up, down, left, right]