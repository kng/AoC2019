# --- Day 3: Squares With Three Sides ---
# https://adventofcode.com/2016/day/3

import time
import re
simple = False
verbose = 1

if simple:
    data = '5 10 25\n3 3 3\n3 3 4\n3 3 6'.splitlines()
else:
    file = open('03_input.txt', 'r')
    data = file.read().splitlines()


def main():
    start_time = time.time()

    if verbose > 2:
        print('data:{}'.format(data))

    # part 1
    valid = 0
    for row in data:
        tri = [int(x) for x in re.split(r'\s+', row.lstrip())]
        if tri[0] + tri[1] > tri[2] and tri[0] + tri[2] > tri[1] and tri[1] + tri[2] > tri[0]:
            valid += 1
            if verbose > 2:
                print('valid: {}'.format(row))
        elif verbose > 2:
            print('invalid: {}'.format(row))
    print('total valid: {}'.format(valid))

    middle_time = time.time()
    print("part 1 time elapsed: {} seconds".format(middle_time - start_time))

    # part 2
    i = valid = 0
    print('rows {}'.format(len(data)))
    while i < len(data):
        r1 = data[i]
        r2 = data[i+1]
        r3 = data[i+2]
        t1 = [int(x) for x in re.split(r'\s+', r1.lstrip())]
        t2 = [int(x) for x in re.split(r'\s+', r2.lstrip())]
        t3 = [int(x) for x in re.split(r'\s+', r3.lstrip())]
        for j in range(3):
            if t1[j] + t2[j] > t3[j] and t1[j] + t3[j] > t2[j] and t2[j] + t3[j] > t1[j]:
                valid += 1
        i += 3
    print('total valid: {}'.format(valid))
    # 1025 too low

    end_time = time.time()
    print("part 2 time elapsed: {} seconds".format(end_time - middle_time))


if __name__ == '__main__':
    main()
