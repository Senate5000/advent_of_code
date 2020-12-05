def split_row_col_list(list_len, row_id, lower_half_val, upper_half_val):
    base_row_list = [x for x in range(list_len)]
    for x in row_id:
        half_list = int(len(base_row_list) / 2)
        if x == lower_half_val:
            base_row_list = base_row_list[0:half_list]
        elif x == upper_half_val:
            base_row_list = base_row_list[half_list:]
    return base_row_list[0] # probably a better way to get just one element out of a list

def find_seat_id(seat_ids):
    seat_ids.sort()
    for idx, seat_id in enumerate(seat_ids):
        if idx == len(seat_ids):
            # we should never get here, but the below code will also fail with index out of range
            break
        if seat_ids[idx + 1] == (seat_id + 2):
            return seat_id + 1



test_input = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
seat_ids = []
with open("./input/day_5_part_1.txt") as f:
# with open("./input/day_5_sample_data.txt") as f:
    for line in f:
        stripped_line = line.strip()
        print(stripped_line)
        rows = stripped_line[0:7]
        cols = stripped_line[7:]
        print(rows)
        print(cols)

        row_id = split_row_col_list(128, rows, "F", "B")
        print(f"row_id: {row_id}")
        col_id = split_row_col_list(8, cols, "L", "R")
        print(f"col_id: {col_id}")

        seat_id = (row_id * 8 + col_id)
        seat_ids.append(int(seat_id))
        print(seat_id)

print(max(seat_ids))
print(find_seat_id(seat_ids))
