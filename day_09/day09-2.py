DEBUG = False

if DEBUG:
    file = open("day_09_input_test.txt", "r")
else:
    file = open("day_09_input.txt", "r")
original_data = file.read().strip().split("\n")
file.close()

input_sequences = []
input_idx = 0

for line in original_data:
    input_sequences.append([])
    for _t in line.strip().split(' '):
        input_sequences[input_idx].append(int(_t))
    
    input_idx += 1

total = 0

for idx in range(len(input_sequences)):
    # if DEBUG:
    #     print("$"* 50)
    #     print("Working on seq", input_sequences[idx])
    #     print("$"* 50)

    working_seq = []
    working_seq.append(input_sequences[idx])

    seq_depth = 0

    while sum(working_seq[seq_depth]) != 0:
        working_seq.append([])

        for idx_inner in range(len(working_seq[seq_depth]) - 1):
            working_seq[seq_depth+1].append(working_seq[seq_depth][idx_inner+1] - working_seq[seq_depth][idx_inner])

        seq_depth += 1

    extrapolated_vals = [0]

    while seq_depth > 0:
        seq_depth-=1

        extrapolated_vals.insert(0, working_seq[seq_depth][0] - extrapolated_vals[0])

    #print(extrapolated_vals)
    
    total += extrapolated_vals[0]

print(total)