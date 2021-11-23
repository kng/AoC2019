# --- Day 7: Internet Protocol Version 7 ---
# https://adventofcode.com/2016/day/7

import re
import time
simple = False
verbose = 1

if simple:
    data = ['abba[mnop]qrst', 'abcd[bddb]xyyx',
            'aaaa[qwer]tyui', 'ioxxoj[asdfgh]zxcvbn',
            'aba[bab]xyz', 'xyx[xyx]xyx', 'aaa[kek]eke', 'zazbz[bzb]cdb']
else:
    file = open('07_input.txt', 'r')
    data = file.read().splitlines()


def main():
    start_time = time.time()

    # part 1
    p = re.compile(r'\[(\w+)]')
    supported = 0
    for row in data:
        a = p.split(row)
        c = check_abba(a)
        if verbose > 2:
            print('row {}'.format(row))
            print('row split {}'.format(a))
            print('checked {}'.format(c))
        if 1 in c[1:][::2]:  # even, inside brackets
            if verbose > 2:
                print('abba within hypernet')
            continue
        elif 1 in c[::2]:    # odd, outside brackets
            supported += 1
            if verbose > 2:
                print('tls supported')
    print('part 1: {}'.format(supported))

    middle_time = time.time()
    print("part 1 time elapsed: {} seconds".format(middle_time - start_time))

    # part 2
    supported = 0
    for row in data:
        a = p.split(row)
        b = find_aba(a[::2])      # odd, outside brackets
        c = find_aba(a[1:][::2])  # even, inside brackets
        if verbose > 2:
            print('row {}'.format(row))
            print('found {} and {}'.format(b, c))
        for aba in b:
            bab = ''.join([aba[1], aba[0], aba[1]])
            if bab in c:
                supported += 1
                break
    print('part 2: {}'.format(supported))

    end_time = time.time()
    print("part 2 time elapsed: {} seconds".format(end_time - middle_time))


def check_abba(word):
    ret = []
    for w in word:
        abba = 0
        if len(w) > 3:
            for i in range(len(w) - 3):
                if w[i] == w[i + 3] and w[i + 1] == w[i + 2] and w[i] != w[i + 1]:
                    abba = 1
                    break
        ret.append(abba)
    return ret


def find_aba(word):
    ret = []
    for w in word:
        if len(w) > 2:
            for i in range(len(w) - 2):
                if w[i] == w[i + 2] and w[i] != w[i + 1]:
                    ret.append(w[i:i+3])
    return ret


if __name__ == '__main__':
    main()
