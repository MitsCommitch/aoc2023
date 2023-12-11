from functools import reduce
from itertools import chain
import sys

def translate(start, mapper):
    nxt, curr, rng = mapper

    if start in range(curr, curr+rng):
        return nxt + (start - curr)
    return start

def part_a(lines):
    seed_list = lines[0].split()[1:]

    lowest = None
    maps = {}
    map_name = ""
    for line in lines[1:]:
        if line.endswith('map:'):
            map_name = line.split()[0]
            maps[map_name] = []
        elif line and line[0].isdigit():
            dest, src, rng = map(lambda x: int(x),line.split())
            maps[map_name].append((range(src, src+rng), dest-src))

    for seed in seed_list:
        curr = int(seed)
        for src_to_dest in maps.values():
            for mapping in src_to_dest:
                rng, diff = mapping
                if curr in rng:
                    curr += diff
                    break

        if not lowest or curr < lowest:
            lowest = curr

    print(f'Lowest Location number: {lowest}')

def part_b(lines):
    seed_list = lines[0].split()[1:]
    seed_ranges = [range(int(x), int(x)+int(y)) for x, y in zip(seed_list[::2], seed_list[1::2])]

    maps = {}
    map_name = ""
    working_set = seed_ranges
    hits = []
    misses = []
    next_working_set = []
    for line in lines[1:]:
        if hits:
            for hit in hits:
                working_set.remove(hit)
            hits = []
        if line.endswith('map:'):
            working_set += next_working_set
            next_working_set = []
            map_name = line.split()[0]
            maps[map_name] = []
        elif line and line[0].isdigit():
            dest, src, rng = map(lambda x: int(x),line.split())
            mapping_range, diff = (range(src, src+rng), dest-src)
            for prop_range in working_set:
                if prop_range.start <= mapping_range.stop and prop_range.stop >= mapping_range.start:
                    hit_range = range(max(prop_range.start, mapping_range.start), min(prop_range.stop, mapping_range.stop))
                    hits.append(prop_range)
                    if prop_range.start < hit_range.start:
                        misses.append(range(prop_range.start, hit_range.start))
                    if prop_range.stop > hit_range.stop:
                        misses.append(range(hit_range.stop, prop_range.stop))
                    next_working_set.append(range(hit_range.start+diff, hit_range.stop+diff))
            working_set += misses
            misses = []

    working_set += next_working_set
    lowest = list(map(lambda x: x.start, working_set))
    print(f'Lowest Location number: {min(lowest)}')


def today(lines):
    part_a(lines)
    part_b(lines)
