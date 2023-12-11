import re
import sys

def get_nums(line):
    nlt = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }

    res = []
    for num in nlt.keys():
        hits = re.finditer(num, line)
        for hit in hits:
            res.append((nlt[num], hit.start()))
    if res:
        return  [min(res, key=lambda x:x[1]), max(res, key=lambda x:x[1])]

def get_calib_from_line_a(line):
    nums = [d for d in line if d.isdigit()]
    return int(f'{nums[0]}{nums[-1]}')

def get_calib_from_line_b(line):
    digits = list(filter(str.isdigit, line))
    if digits:
        first, last = (digits[0], digits[-1])
        fi, li = (line.find(first), line.rfind(last))
    else:
        return 0
    wordnums = get_nums(line)
    if wordnums:
        fw, fwi = wordnums[0]
        if fi > fwi:
            first = fw

        lw, lwi = wordnums[1]
        if li < lwi:
            last = lw

    return int(f'{first}{last}')

def part_a(lines):
    sum = 0

    for line in lines:
        sum += get_calib_from_line_a(line)

    print(f'Part A sum was: {sum}.')

def part_b(lines):
    sum = 0

    for line in lines:
        sum += get_calib_from_line_b(line)

    print(f'Part B sum was {sum}.')

def today(lines):
    part_a(lines)
    part_b(lines)
