# with open("./input/day6_sample_input.txt") as f:
def part_one(input):
    with open(input) as f:
        group_totals = []
        group_set = set()
        for line in f:
            stripped_line = line.strip()
            if stripped_line:
                for c in stripped_line:
                    group_set.add(c)
            else:
                group_totals.append(len(group_set))
                group_set = set()
        group_totals.append(len(group_set)) # hacky way to get last group
    return sum(group_totals)

def part_two(input):
    with open(input) as f:
        group_totals = []
        group = [] # this will hold many sets
        for line in f:
            stripped_line = line.strip()
            if stripped_line:
                line_set = set(stripped_line)
                group.append(line_set)
            else:
                group_intersection = group[0].intersection(*group)
                if group_intersection:
                    group_totals.append(len(group_intersection))
                group = []
        group_intersection = group[0].intersection(*group)
        if group_intersection:
            group_totals.append(len(group_intersection))

        return sum(group_totals)

def main():
    # file_input = "./input/day6_sample_input.txt"
    file_input = "./input/day6_input.txt"
    part_one_results = part_one(file_input)
    part_two_results = part_two(file_input)

    print(f"Part One: {part_one_results}")
    print(f"Part Two: {part_two_results}")

if __name__ == "__main__":
    main()
