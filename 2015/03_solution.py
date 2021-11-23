# --- Day 3: Perfectly Spherical Houses in a Vacuum ---
# https://adventofcode.com/2015/day/3

import time
import numpy as np
simple = False
verbose = 0

if simple:
    data = '^v^v^v^v^v'
    fieldWidth = 5
else:
    file = open('03_input.txt', 'r')
    data = file.read().strip()
    fieldWidth = 1000


def main():
    start_time = time.time()

    # part 1
    field = np.zeros((fieldWidth, fieldWidth), dtype=np.uint8)
    x = y = int(fieldWidth / 2)
    field[y, x] += 1
    for d in data:
        if verbose > 1:
            print('move: {}'.format(d))
        if d == '^':
            y += 1
        if d == 'v':
            y -= 1
        if d == '>':
            x += 1
        if d == '<':
            x -= 1
        field[y, x] = 1
    n = field > 0
    print('part 1, houses receiving at least one present:\n {}'.format(n.sum()))

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    # part 2
    field = np.zeros((fieldWidth, fieldWidth), dtype=np.uint8)
    x1 = x2 = y1 = y2 = int(fieldWidth / 2)
    field[y1, x1] += 1
    field[y2, x2] += 1
    i = False
    for d in data:
        if verbose > 1:
            print('move: {}'.format(d))
        if d == '^':
            if i:
                y1 += 1
            else:
                y2 += 1
        if d == 'v':
            if i:
                y1 -= 1
            else:
                y2 -= 1
        if d == '>':
            if i:
                x1 += 1
            else:
                x2 += 1
        if d == '<':
            if i:
                x1 -= 1
            else:
                x2 -= 1
        if i:
            field[y1, x1] = 1
            i = False
        else:
            field[y2, x2] = 1
            i = True
    n = field > 0
    print('part 2, houses receiving at least one present:\n {}'.format(n.sum()))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
