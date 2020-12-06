# with open("./input/day6_sample_input.txt") as f:
def do_set_stuff(group, version):
    modified_group = []
    if version == 1:
        modified_group = set.union(*group)
    elif version == 2:
        modified_group = set.intersection(*group)
    return len(modified_group)

def check_input(input, version):
    with open(input) as f:
        group_totals = []
        group = []
        for line in f:
            stripped_line = line.strip()
            if stripped_line:
                group.append(set(stripped_line))
            else:
                group_len = do_set_stuff(group, version)
                group_totals.append(group_len)
                group = []
        group_totals.append(do_set_stuff(group, version)) # hacky way to get last group
    return sum(group_totals)

def main():
    # file_input = "./input/day6_sample_input.txt"
    file_input = "./input/day6_input.txt"
    part_one_results = check_input(file_input, 1)
    part_two_results = check_input(file_input, 2)

    print(f"Part One: {part_one_results}")
    print(f"Part Two: {part_two_results}")

if __name__ == "__main__":
    main()
