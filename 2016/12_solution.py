# --- Day 12: Leonardo's Monorail ---
# https://adventofcode.com/2016/day/12

import time
simple = False
verbose = 1

if simple:
    data = ['cpy 41 a', 'inc a', 'inc a', 'dec a', 'jnz a 2', 'dec a']
else:
    file = open('12_input.txt', 'r')
    data = file.read().splitlines()


def main():
    start_time = time.time()

    # part 1/2
    reg = {'a': 0, 'b': 0, 'c': 0, 'd': 0}  # cpu registers
    inst = ['cpy', 'inc', 'dec', 'jnz']  # valid instructions
    if simple:
        print('data:\n{}'.format(data))

    part = 1  # set this to 1 or 2
    if part == 2:
        reg['c'] = 1
    pp = 0
    while pp < len(data):
        a = data[pp].split(' ')
        if a[0] in inst:  # check if valid instruction
            if a[0] == 'cpy' and len(a) == 3:  # cpy imm/reg reg
                if a[1].isnumeric():
                    reg[a[2]] = int(a[1])
                else:
                    reg[a[2]] = reg[a[1]]
            if a[0] == 'inc' and len(a) == 2:  # inc reg
                reg[a[1]] += 1
            if a[0] == 'dec' and len(a) == 2:  # dec reg
                reg[a[1]] -= 1
            if a[0] == 'jnz' and len(a) == 3:  # jnz reg/imm imm, if val not zero
                if a[1].isnumeric():
                    if a[1] != 0:
                        pp += int(a[2])
                        continue
                else:
                    if reg[a[1]] != 0:
                        pp += int(a[2])
                        continue
        pp += 1
    print('part {} register a {}'.format(part, reg['a']))

    end_time = time.time()
    print("part {} time elapsed: {} seconds".format(part, end_time - start_time))


if __name__ == '__main__':
    main()
