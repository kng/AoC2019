# --- Day 2: I Was Told There Would Be No Math ---
# https://adventofcode.com/2015/day/2

import time
simple = False
verbose = 0

if simple:
    data = ['2x4x3', '1x1x10']
else:
    file = open('02_input.txt', 'r')
    data = file.read().splitlines()


def main():
    start_time = time.time()
    total_p = 0
    total_r = 0
    for present in data:
        paper = [int(n) for n in present.split('x')]
        paper.sort()
        if len(paper) != 3:
            print('Bad paper format')
            break
        sides = [paper[0]*paper[1], paper[1]*paper[2], paper[0]*paper[2]]
        sides.sort()
        area = 3 * sides[0] + 2 * sides[1] + 2 * sides[2]
        ribbon = 2 * paper[0] + 2 * paper[1] + paper[0] * paper[1] * paper[2]
        total_p += area
        total_r += ribbon
        if verbose > 0:
            print('Present: {}'.format(paper), end=', ')
            print('Min area: {}'.format(sides[0]), end=', ')
            print('Wrapping area: {}'.format(area), end=', ')
            print('Ribbon: {}'.format(ribbon))

    print('Order: {} sqf of wrapping paper'.format(total_p))
    print('And {} feet of ribbon'.format(total_r))

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
