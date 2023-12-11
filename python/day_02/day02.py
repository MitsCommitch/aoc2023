from functools import reduce
import re
import sys

JUST_TEXT = re.compile(r'[\W_ ]+', re.UNICODE)

def part_a(lines):
    cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
    }

    sum = 0

    for line in lines:
        id, games = line.split(':')
        id = int(id.split()[1])
        plays = games.strip().split(' ')
        play_list = list(map(lambda p: (p[0], ''.join(filter(str.isalpha, p[1]))), zip(plays[::2], plays[1::2])))
        for play in play_list:
            if int(play[0]) > cubes[play[1]]:
                id = 0
                break

        sum += id
    
    print(f'Part A sum was: {sum}')

def part_b(lines):
    min_cubes = {
        "green": 0,
        "red": 0,
        "blue": 0
    }

    pow = 0

    for line in lines:
        _, games = line.split(':')
        plays = games.strip().split(' ')
        play_list = list(map(lambda p: (int(p[0]), ''.join(filter(str.isalpha, p[1]))), zip(plays[::2], plays[1::2])))
        for play in play_list:
            if min_cubes[play[1]] < play[0]:
                min_cubes[play[1]] = play[0]

        pow += reduce((lambda x, y: x*y), min_cubes.values())
        min_cubes = {
            "green": 0,
            "red": 0,
            "blue": 0
        }

    print(f'Power of mins is: {pow}')

def today(lines):
    part_a(lines)
    part_b(lines)
