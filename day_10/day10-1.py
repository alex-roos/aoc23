DEBUG = False

class PipeNode:

    connected_pipes = set()
    loc = (-1, -1)

    def __init__(self, row, col):
        self.connected_pipes = set()
        self.loc = (row, col)

    def add_connection(self, _in):
        self.connected_pipes.add(_in)

def update_connections(start_node, new_connect_locations):
    for _connection in new_connect_locations:
        if _connection[0] >= 0 and _connection[0] <= 139 and _connection[1] >= 0 and _connection[1] <= 139:
            start_node.add_connection(pipe_dict[_connection])

            pipe_dict[_connection].add_connection(start_node)

class PipeTraverser:

    current_node = None
    depth = 0
    visited_nodes = []
    frontier = []

    def __init__(self, _s, _d, _v, _f):
        self.current_node = _s
        self.depth = _d
        self.visited_nodes = _v
        self.frontier = _f

    def replicate(self):
        return PipeTraverser(self.current_node, self.depth, self.visited_nodes.copy(), self.frontier.copy())


if DEBUG:
    file = open("C:\\Users\\alexr\\git\\aoc23\\day_10\\day_10_input_test.txt", "r")
else:
    file = open("day_10_input.txt", "r")
original_data = file.read().strip().split("\n")
file.close()

count_rows = len(original_data)
count_col = len(original_data[0])

pipe_dict = dict()

for _row in range(count_rows):
    for _col in range(count_col):
        pipe_dict[(_row, _col)] = PipeNode(_row, _col)

curr_row = 0
for line in original_data:
    #print("Row", curr_row, ':', line)
    for _col, _token in enumerate(line):

        connections_to_add = []
        if _token == '|':
            # above and below
            connections_to_add.append((curr_row - 1, _col))
            connections_to_add.append((curr_row + 1, _col))
        elif _token == '-':
            # left and right
            connections_to_add.append((curr_row, _col - 1))
            connections_to_add.append((curr_row, _col + 1))
        elif _token == 'L':
            # above and right
            connections_to_add.append((curr_row - 1, _col))
            connections_to_add.append((curr_row, _col + 1))
        elif _token == 'J':
            # above and left
            connections_to_add.append((curr_row - 1, _col))
            connections_to_add.append((curr_row, _col - 1))
        elif _token == '7':
            # below and left
            connections_to_add.append((curr_row + 1, _col))
            connections_to_add.append((curr_row, _col - 1))
        elif _token == 'F':
            # below and right
            connections_to_add.append((curr_row + 1, _col))
            connections_to_add.append((curr_row, _col + 1))
        elif _token == 'S':
            start = (curr_row, _col)

        #print("Connections to add:", connections_to_add)

        update_connections(pipe_dict[(curr_row, _col)], connections_to_add)    

    curr_row += 1

#print("Start neighbors are:", pipe_dict[start].connected_pipes)

# _r = 1
# for _c in range(5):
#     print("Row", _r, "Col", _c, "Neighbors:", [x.loc for x in pipe_dict[(_r, _c)].connected_pipes])

result_map = [['.']*5]*5

traversers = [PipeTraverser(pipe_dict[start], 0, [pipe_dict[start]], list(pipe_dict[start].connected_pipes))]

path_depths = []
full_visited_set = set()
full_visited_set.add(pipe_dict[start])

while len(traversers) > 0:
    next_depth_of_traversers = []

    if traversers[0].depth % 100 == 0:
        print("Current depth:", traversers[0].depth)

    for _next_mover in traversers:
        new_traversers = []

        if len(_next_mover.frontier) == 0:
            path_depths.append(_next_mover.depth)
        elif len(_next_mover.frontier) == 1:
            new_traversers = [_next_mover]
        elif len(_next_mover.frontier) > 1:
            temp_frontier = _next_mover.frontier.copy()

            new_traversers.append(_next_mover)

            for i in range(len(_next_mover.frontier) - 1):
                new_traversers.append(_next_mover.replicate())

            assert(len(temp_frontier) == len(new_traversers))

            for _idx in range(len(temp_frontier)):
                new_traversers[_idx].frontier = [temp_frontier[_idx]]

        for pipe_traversal in new_traversers:
            pipe_traversal.depth += 1
            #result_map[pipe_traversal.current_node.loc[0]][pipe_traversal.current_node.loc[1]] = pipe_traversal.depth
            pipe_traversal.current_node = pipe_traversal.frontier[0]
            pipe_traversal.visited_nodes.append(pipe_traversal.current_node)
            full_visited_set.add(pipe_traversal.current_node)
            
            pipe_traversal.frontier = []
            for _pipe in pipe_traversal.current_node.connected_pipes:
                if _pipe not in pipe_traversal.visited_nodes and _pipe not in full_visited_set:
                    pipe_traversal.frontier.append(_pipe)
            
            next_depth_of_traversers.append(pipe_traversal)

    traversers = next_depth_of_traversers  
                
# for row in result_map:
#     print(row)

print("Final depths:", path_depths)