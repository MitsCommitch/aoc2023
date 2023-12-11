import argparse
from datetime import datetime as dt
import os
import re
import sys

def init_arg_parse():
    parser = argparse.ArgumentParser()
    parser.add_argument('day')

    return parser

def main(argv):
    parser = init_arg_parse()
    args = parser.parse_args()

    with open(f'./day_{args.day}/input.txt') as f:
        input = f.read()
        split_input = input.splitlines()

    match args.day:
        case '01':
            from day_01 import day01
            day01.today(split_input)

        case '02':
            from day_02 import day02
            day02.today(split_input)

        case '03':
            from day_03 import day03
            day03.today(split_input)

        case '04':
            from day_04 import day04
            day04.today(split_input)

        case '05':
            from day_05 import day05
            day05.today(split_input)

        case '06':
            from day_06 import day06
            day06.today(split_input)

        case _:
            return
        


if __name__ == "__main__":
    main(sys.argv)