# --- Day 1: Not Quite Lisp ---
# https://adventofcode.com/2015/day/1

import time
simple = False
verbose = 1

if simple:
    data = '(()(()('
else:
    file = open('01_input.txt', 'r')
    data = file.read().strip()


def main():
    start_time = time.time()
    floor = 0
    pos = 0
    base = 0
    for m in data:
        pos += 1
        if m == '(':
            floor += 1
        if m == ')':
            floor -= 1
        if floor == -1 and base == 0:
            base = pos

    print('Floor {}'.format(floor))
    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    print('Pos {}'.format(base))
    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
