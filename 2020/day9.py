def get_possible_combinations(inputs):
    combinations = set()
    for x in range(len(inputs) - 1):
        for y in inputs[x:]:
            combinations.add(inputs[x] + y)
    return combinations

def check_validity(preamble, input):
    all_lines = [int(line.strip()) for line in f]

    for x, y in enumerate(input):
        if x + 1 > preamble:
            input_to_check = input[x-preamble:x]
            valid_inputs = get_possible_combinations(input_to_check)
            if y not in valid_inputs:
                return y

def get_continguous_set(val, input):
    previous_vals = []
    def get_min_max_sum():
        return min(previous_vals) + max(previous_vals)

    for x in input:
        previous_vals.append(x)
        previous_vals_sum = sum(previous_vals)
        if previous_vals_sum == val:
            return get_min_max_sum()
        elif previous_vals_sum > val:
            while sum(previous_vals) > val:
                previous_vals.pop(0)
                if sum(previous_vals) == val:
                    return get_min_max_sum()

# input_file = "./input/day9_sample_input.txt"
input_file = "./input/day9_input.txt"
with open(input_file) as f:
    all_lines = [int(line.strip()) for line in f]
    bad_value = check_validity(25, all_lines)
    print(f"Bad Value: {bad_value}")
    encryption_weakness = get_continguous_set(bad_value, all_lines)
    print(f"Encryption Weakness: {encryption_weakness}")