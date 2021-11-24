# --- Day 8: Two-Factor Authentication ---
# https://adventofcode.com/2016/day/8

import numpy
import re
import time
simple = False
verbose = 1

if simple:
    # noinspection SpellCheckingInspection
    data = ['rect 3x2', 'rotate column x=1 by 1', 'rotate row y=0 by 4', 'rotate column x=1 by 1']
    size = {'x': 7, 'y': 3}
else:
    file = open('08_input.txt', 'r')
    data = file.read().splitlines()
    size = {'x': 50, 'y': 6}


def main():
    start_time = time.time()

    rect = re.compile(r'rect (\d+)x(\d+)', flags=re.IGNORECASE)
    rota = re.compile(r'rotate \w+ (\w)=(\d+) by (\d+)', flags=re.IGNORECASE)
    kp = numpy.full((size['y'], size['x']), False)

    if verbose > 2:
        print('data:\n{}'.format(data))
    if simple:
        print(kp)

    # part 1
    for row in data:
        if verbose > 1:
            print(row)
        inst = rect.match(row)
        if inst:
            kp[0:int(inst.group(2)), 0:int(inst.group(1))] = True
        inst = rota.match(row)
        if inst:
            if inst.group(1) == 'x':
                kp[:, int(inst.group(2))] = numpy.roll(kp[:, int(inst.group(2))], int(inst.group(3)))
            else:
                kp[int(inst.group(2))] = numpy.roll(kp[int(inst.group(2))], int(inst.group(3)), axis=0)
    print('part 1: lit pixels {}'.format(kp.sum()))

    middle_time = time.time()
    print("part 1 time elapsed: {} seconds".format(middle_time - start_time))

    # part 2
    for row in kp:
        for col in row:
            if col:
                print('#', end='')
            else:
                print(' ', end='')
        print('')

    end_time = time.time()
    print("part 2 time elapsed: {} seconds".format(end_time - middle_time))


if __name__ == '__main__':
    main()
