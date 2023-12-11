from functools import reduce
import re
import sys

nos = re.compile(r'\d+')
pts = re.compile(r'[^\d.]')

def process_schematic(schematic):
    lineno = 1
    parts = []
    numbers = []
    for line in schematic:
        parts += list(map(lambda m: (lineno, m.start(), m.end(), m.group()), pts.finditer(line) ))
        numbers += list(map(lambda m: (lineno, m.start(), m.end(), m.group()), nos.finditer(line) ))
        lineno += 1

    return parts, numbers

def filter_partnos(part, number):
    if number[0]-1 <= part[0] <= number[0]+1:
        if number[1]-1 <= part[1] <= number[2]:
            return True

def get_valid_parts(parts, numbers):
    hits = []
    for part in parts:
        hits += list(filter(lambda n: filter_partnos(part, n), numbers))

    return set(hits)      

def check_gears(parts, numbers):
    gears = []
    potential_gears = [g for g in parts if g[3] == '*']
    for gear in potential_gears:
        gear_parts = list(filter(lambda n: filter_partnos(gear, n), numbers))
        if len(gear_parts) == 2:
            gears.append((int(gear_parts[0][3]), int(gear_parts[1][3])))

    return gears

def get_ratios(gears):
    ratios = list(map(lambda g: g[0]*g[1], gears))
    return ratios

def part_a(lines):
    parts, numbers = process_schematic(lines)
    valid_parts = get_valid_parts(parts, numbers)

    if valid_parts:
        res = sum(int(n[3]) for n in valid_parts)
        print(f'Sum of part nos is: {res}') 
        return
    
    print(f'No valid parts.')

def part_b(lines):
    parts, numbers = process_schematic(lines)
    gears = check_gears(parts, numbers)
    if gears:
        ratios = get_ratios(gears)
        if ratios:
            res = sum(ratios)
            print(f'Sum of ratios is: {res}')
    return

def today(lines):
    part_a(lines)
    part_b(lines)
