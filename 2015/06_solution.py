# --- Day 6: Probably a Fire Hazard ---
# https://adventofcode.com/2015/day/6

import numpy
import re
import time
simple = False
verbose = 1

if simple:
    data = ['turn on 0,0 through 999,999',
            'toggle 0,0 through 999,0',
            'turn off 499,499 through 500,500']
else:
    file = open('06_input.txt', 'r')
    data = file.read().splitlines()


def main():
    start_time = time.time()

    inst = re.compile(r'(\d+),(\d+) through (\d+),(\d+)')
    size = 1000
    lights1 = numpy.full((size, size), False)
    for row in data:
        a = inst.split(row)
        x1 = int(a[1])
        y1 = int(a[2])
        x2 = int(a[3])+1
        y2 = int(a[4])+1
        if 'turn on' in a[0]:
            lights1[x1:x2, y1:y2] = True
        elif 'turn off' in a[0]:
            lights1[x1:x2, y1:y2] = False
        elif 'toggle' in a[0]:
            lights1[x1:x2, y1:y2] ^= True
        else:
            print('unknown')
    print('part 1 lights lit {}'.format(lights1.sum()))

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    lights2 = numpy.full((size, size), 0)
    for row in data:
        a = inst.split(row)
        x1 = int(a[1])
        y1 = int(a[2])
        x2 = int(a[3])+1
        y2 = int(a[4])+1
        if 'turn on' in a[0]:
            lights2[x1:x2, y1:y2] += 1
        elif 'turn off' in a[0]:
            lights2[x1:x2, y1:y2] -= 1
            numpy.clip(lights2, 0, 9999, out=lights2)
        elif 'toggle' in a[0]:
            lights2[x1:x2, y1:y2] += 2
        else:
            print('unknown')
    print('part 2 lights brightness {}'.format(lights2.sum()))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
