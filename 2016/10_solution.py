# --- Day 10: Balance Bots ---
# https://adventofcode.com/2021/day/10

import time
import re
simple = False
verbose = 0

if simple:
    data = ['value 5 goes to bot 2',
            'bot 2 gives low to bot 1 and high to bot 0',
            'value 3 goes to bot 1',
            'bot 1 gives low to output 1 and high to bot 0',
            'bot 0 gives low to output 2 and high to output 0',
            'value 2 goes to bot 2']
    responsible = [5, 3]
else:
    file = open('10_input.txt', 'r')
    data = file.read().splitlines()
    responsible = [61, 17]


def main():
    start_time = time.time()
    bc = re.compile(r'bot (\d+)')
    bg = re.compile(r'bot (\d+) gives low to (\w+) (\d+) and high to (\w+) (\d+)')
    bv = re.compile(r'value (\d+) goes to bot (\d+)')

    # part 1
    bmax = 0
    for row in data:  # find max bot number
        if verbose > 1:
            print(row)
        a = [int(i) for i in bc.findall(row)]
        bmax = max(bmax, max(a))

    bots = [[-1, -1, -1, -1] for _ in range(bmax + 1)]  # allocate bots
    val = []
    for row in data:
        a = bg.match(row)
        if a:
            bot = int(a.group(1))
            bots[bot][2] = int(a.group(3)) if a.group(2) == 'bot' else int(a.group(3)) + 1000
            bots[bot][3] = int(a.group(5)) if a.group(4) == 'bot' else int(a.group(5)) + 1000
        a = bv.match(row)
        if a:
            val.append([int(i) for i in a.groups()])

    while len(val) > 0:  # loop through and add to the values
        v, bot = val.pop(0)
        if bots[bot][0] == -1:
            bots[bot][0] = v
        else:
            bots[bot][1] = v
            if verbose > 2:
                print('min {} goes to {}, max {} goes to {}'
                      .format(min(bots[bot][0:2]), bots[bot][2], max(bots[bot][0:2]), bots[bot][3]))
            if bots[bot][3] < 1000:
                val.append([max(bots[bot][0:2]), bots[bot][3]])
            if bots[bot][2] < 1000:
                val.append([min(bots[bot][0:2]), bots[bot][2]])

    if simple:
        for i in range(len(bots)):
            print('bot {}: {}'.format(i, bots[i]))

    for bot in range(len(bots)):
        if responsible[0] in bots[bot][0:2] and responsible[1] in bots[bot][0:2]:
            print('part 1, found {} and {} in bot {}'.format(responsible[0], responsible[1], bot))

    middle_time = time.time()
    print("part 1 time elapsed: {} seconds".format(middle_time - start_time))

    # part 2
    prod = 1
    for bot in range(len(bots)):
        for i in range(1000, 1003):  # find product of output 0 * 1 * 2
            if bots[bot][2] == i:
                prod *= min(bots[bot][0:2])
            if bots[bot][3] == i:
                prod *= max(bots[bot][0:2])
    print('part 2, product {}'.format(prod))

    end_time = time.time()
    print("part 2 time elapsed: {} seconds".format(end_time - middle_time))


if __name__ == '__main__':
    main()
