# --- Day 4: Security Through Obscurity ---
# https://adventofcode.com/2016/day/4

import time
import re
import string
simple = False
verbose = 1

if simple:
    data = ['aaaaa-bbb-z-y-x-123[abxyz]',
            'a-b-c-d-e-f-g-h-987[abcde]',
            'not-a-real-room-404[oarel]',
            'totally-real-room-200[decoy]']
else:
    file = open('04_input.txt', 'r')
    data = file.read().splitlines()  # multi line

p = re.compile(r'-(\d+)\[(\w+)\]')


def main():
    start_time = time.time()

    # part 1
    sector = 0
    rooms = []
    for row in data:
        ltr = {a: 0 for a in string.ascii_lowercase}
        a = p.split(row)  # ['a-b-c-d-e-f-g-h', '987', 'abcde', '']
        for b in a[0]:
            if b.isalpha():
                ltr[b] += 1
        chk = ''
        for i in reversed(range(1, max(ltr.values()) + 1)):
            for j in ltr.keys():
                if ltr[j] == i:
                    chk += j
        if a[2] in chk:
            sector += int(a[1])
            rooms.append([a[0], a[1]])
            if verbose > 1:
                print('nice {}'.format(a[0]))
        elif verbose > 1:
            print('naughty {}'.format(a[0]))
    print('sector sum {}'.format(sector))

    middle_time = time.time()
    print("part 1 time elapsed: {} seconds".format(middle_time - start_time))

    # part 2
    if simple:
        rooms.append(['qzmt-zixmtkozy-ivhz-343', '343'])

    al = list(string.ascii_lowercase)
    for row, key in rooms:
        dec = ''
        for i in row:
            if i.isalpha():
                dec += al[(al.index(i) + int(key)) % len(al)]
            else:
                dec += ' '
        if 'northpole' in dec or simple:
            print('{} {}'.format(key, dec))

    end_time = time.time()
    print("part 2 time elapsed: {} seconds".format(end_time - middle_time))


if __name__ == '__main__':
    main()
