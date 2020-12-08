# input_file = "./input/day8_sample_input.txt"
input_file = "./input/day8_input.txt"
with open(input_file) as f:
    all_lines = [line.strip() for line in f]

    def get_v1_result(lines=all_lines):
        executed_lines = []
        idx = 0
        acc = 0
        while idx not in executed_lines:
            command, amount = lines[idx].split(" ")
            executed_lines.append(idx)
            if command == "nop":
                idx += 1
            if command == "jmp":
                idx += int(amount)
            if command == "acc":
                acc += int(amount)
                idx += 1
            if idx >= len(lines):
                # we're past the end so return what we have
                break
        return (executed_lines, acc)

    def get_v2_result():
        attempted_swaps = []
        for x in range(len(all_lines)):
            new_lines = all_lines.copy()
            command, amount = all_lines[x].split(" ")
            if command == "acc":
                continue
            elif command == "jmp":
                new_lines[x] = new_lines[x].replace("jmp", "nop")
            elif command == "nop":
                new_lines[x] = new_lines[x].replace("nop", "jmp")
            results = get_v1_result(new_lines)
            if max(results[0]) == (len(all_lines) - 1):
                print("RESULT FOUND")
                print(results[1])
                break



    print(get_v1_result()[1])
    get_v2_result()