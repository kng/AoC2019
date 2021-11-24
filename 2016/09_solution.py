# --- Day 9: Explosives in Cyberspace ---
# https://adventofcode.com/2021/day/9

import time
import collections
import itertools
simple = False
verbose = 1

if simple:
    # noinspection SpellCheckingInspection
    # data = 'A(1x5)BC'  # ABBBBBC len(7)
    # data = '(3x3)XYZ'  # XYZXYZXYZ len(9)
    # data = 'A(2x2)BCD(2x2)EFG'  # ABCBCDEFEFG len(11)
    # data = '(6x1)(1x3)A'  # (1x3)A len(6)
    # data = 'X(8x2)(3x3)ABCY'  # X(3x3)ABC(3x3)ABCY len(18)
    data = '(27x12)(20x12)(13x14)(7x10)(1x12)A'  # part 2 len(241920)
else:
    file = open('09_input.txt', 'r')
    data = file.read().strip()  # single line


def main():
    start_time = time.time()
    if simple:
        print('data:\n{}'.format(data))

    # part 1
    i = m = 0
    cmd = ''
    dec = ''
    while i < len(data):
        if data[i] == '(':
            m = 1
            cmd = ''
        elif data[i] == ')':
            m = 0
            x, y = map(int, cmd.split('x'))
            dec += data[i+1:i+x+1] * y
            i += x
        elif m == 1:
            cmd += data[i]
        elif m == 0:
            dec += data[i]
        i += 1
    print('part 1, decompressed length: {}'.format(len(dec)))

    middle_time = time.time()
    print("part 1 time elapsed: {} seconds".format(middle_time - start_time))

    if not simple:
        print('part 2 takes too long')
        exit(0)

    # part 2
    i = m = 0
    cmd = ''
    dl = collections.deque(list(data))
    while len(dl) > 0:
        d = dl.popleft()
        if d == '(':
            m = 1
            cmd = ''
        elif d == ')':
            m = 0
            x, y = map(int, cmd.split('x'))
            tmp = list(itertools.islice(dl, 0, x)) * y
            for _ in range(x):
                dl.popleft()
            dl.extendleft(reversed(tmp))
        elif m == 1:
            cmd += d
        elif m == 0:
            i += 1
    print('part 2, decompressed length: {}'.format(i))

    end_time = time.time()
    print("part 2 time elapsed: {} seconds".format(end_time - middle_time))


if __name__ == '__main__':
    main()
