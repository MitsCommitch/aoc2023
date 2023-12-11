import sys

def part_a(lines):
    total = 0
    for line in lines:
        _, nums = line.split(':')
        wn, n = nums.split('|')
    
        hits = set(wn.split()).intersection(set(n.split()))
        if hits:
            total += pow(2, len(hits)-1)

    print(f'Total Score of all winning cards is: {total}')
    return

def part_b(lines):
    res = {}
    for line in lines:
        card, nums = line.split(':')
        _, id = card.split()
        id = int(id)
        wn, n = nums.split('|')
    
        hits = set(wn.split()).intersection(set(n.split()))
        if res.get(id):
            res[id] += 1
        else:
            res[id] = 1
        for card in range(id+1, id+len(hits)+1):
            if res.get(card):
                res[card] += res[id]
            else:
                res[card] = res[id]

    print(f'Total cards after winnings: {sum(res.values())}')

def today(lines):
    part_a(lines)
    part_b(lines)
