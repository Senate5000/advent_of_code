def construct_passport(line, passport):
    print(line)
    split_entries = line.split(" ")
    for key_val in split_entries:
        split_key_val = key_val.split(":")
        print(f"split_key_val: {split_key_val}")
        passport_key = split_key_val[0]
        print(f"passport_key: {passport_key}")
        passport_val = split_key_val[1]
        print(f"passport_val: {passport_val}")
        passport[passport_key] = passport_val
    return passport

def get_valid_passports(passports):
    required_keys = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    for passport in passports:
        print(passport.keys())
        print(required_keys - set(passport.keys()))
    valid_passports = [passport for passport in passports if (not required_keys - set(passport.keys()))]
    return valid_passports

def check_byr(byr):
    return (len(byr) == 4) and (int(byr) >= 1920 and int(byr) <= 2002)

def check_iyr(iyr):
    return (len(iyr) == 4) and (int(iyr) >= 2010 and int(iyr) <= 2020)

def check_eyr(eyr):
    return (len(eyr) == 4) and (int(eyr) >= 2020 and int(eyr) <= 2030)

def check_hgt(hgt):
    is_cm = hgt.endswith("cm")
    is_in = hgt.endswith("in")
    int_hgt = int(hgt.replace("cm", "").replace("in", ""))
    return (is_cm and (int_hgt >= 150 and int_hgt <= 193)) or (is_in and (int_hgt >= 59 and int_hgt <= 76))

def check_hcl(hcl):
    valid_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    is_hex = hcl.startswith("#")
    hex_code = hcl.replace("#", "")
    all_valid_chars = True
    for x in hex_code:
        if x not in valid_characters:
            all_valid_chars = False
            break
    return (is_hex and len(hex_code) == 6 and all_valid_chars)

def check_ecl(ecl):
    valid_ecls = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    return ecl in valid_ecls

def check_pid(pid):
    is_int = pid.isdigit()
    pid_len = len(pid)
    return (is_int and pid_len == 9)

def get_valid_passports_v2(passports):
    func_map = {
        "byr": check_byr,
        "iyr": check_iyr,
        "eyr": check_eyr,
        "hgt": check_hgt,
        "hcl": check_hcl,
        "ecl": check_ecl,
        "pid": check_pid,
    }
    valid_passports = []
    for passport in passports:
        print(passport)
        is_valid = True
        for k, v in passport.items():
            if k == "cid":
                continue
            valid_key = func_map[k](v)
            if not valid_key:
                print(f"Failed Validtion - {k}")
                is_valid = False
                break
        if is_valid:
            valid_passports.append(passport)
    return valid_passports



passports = []
with open("./input/day_4_part_1_input.txt") as f:
    current_passport = {}
    for line in f:
        stripped_line = line.replace("\n", "")
        if not stripped_line: # line is empty
            passports.append(current_passport)
            current_passport = {}
        else:
            current_passport = construct_passport(stripped_line, current_passport)

valid_passports = get_valid_passports(passports)
valid_passports = get_valid_passports_v2(valid_passports)
# create set of required keys
# compare intersection of each set of passport keys against required keys
# count

print(len(valid_passports))
