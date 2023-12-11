from functools import reduce
import operator

def predict_distance(charge, time):
    return charge * (time - charge)

def find_wins(duration, best, start=None, end=None):

    if not start:
        start = 0

    if not end:
        end = duration

    if end == start:
        return end

    charge = int((end+start)/2)

    if end-start <= 2:
        if predict_distance(start, duration) > best:
            return start
        
        if predict_distance(charge, duration) > best:
            return charge
        
        return end

    if predict_distance(charge, duration) > best:
        winning_charge = find_wins(duration, best=best, start=start, end=charge)
    else:
        winning_charge = find_wins(duration, best=best, start=charge, end=end)
    return winning_charge


def part_a(lines):
    durations = map(lambda x: int(x), lines[0].split()[1:])
    bests = map(lambda x: int(x), lines[1].split()[1:])

    wins = []
    for d, b in zip(durations, bests):
        fastest_win = find_wins(d, b)
        wins.append(d-(2*fastest_win)+1)

    if wins:
        res = reduce(operator.mul, wins)
        print(f'{res}')

    return

def part_b(lines):
    duration = int(''.join(lines[0].split()[1:]))
    best = int(''.join(lines[1].split()[1:]))

    fastest_win = find_wins(duration, best)
    ways_to_win = duration-(2*fastest_win)+1
    print(f'{ways_to_win}')
    return


def today(lines):
    part_a(lines)
    part_b(lines)
