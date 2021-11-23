# --- Day 5: How About a Nice Game of Chess? ---
# https://adventofcode.com/2016/day/5

import time
import hashlib
simple = False
verbose = 1

if simple:
    data = 'abc'
else:
    file = open('05_input.txt', 'r')
    data = file.read().strip()


def main():
    start_time = time.time()

    k = '00000'
    pwd = ''
    i = p = 0
    while True:
        s = data + str(i)
        h = hashlib.md5(s.encode()).hexdigest()
        if h[:5] == k:
            pwd += h[5]
            p += 1
            if verbose > 0:
                print('{} {} {}'.format(h[5], s, h))
        if p > 7:
            break
        i += 1
    print(pwd)

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    pwd = ['.', '.', '.', '.', '.', '.', '.', '.']
    i = 0
    while True:
        s = data + str(i)
        h = hashlib.md5(s.encode()).hexdigest()
        if h[:5] == k:
            if h[5].isnumeric():
                j = int(h[5])
                if j < 8 and pwd[j] == '.':
                    pwd[j] = h[6]
            if verbose > 0:
                print('{} {} {} {}'.format(h[5], h[6], s, h))
        if '.' not in pwd:
            break
        i += 1
    print(''.join(pwd))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
