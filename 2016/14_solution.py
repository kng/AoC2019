# --- Day 14: One-Time Pad ---
# https://adventofcode.com/2016/day/14

import time
import hashlib
simple = False
verbose = 0

if simple:
    data = 'abc'
    iterations = 25000
else:
    file = open('14_input.txt', 'r')
    data = file.read().strip()
    iterations = 50000  # somewhere between 25k and 50k should suffice, ymmv :P
    # better solution would be to use a generator, but this completed in less than 2min


def main():
    start_time = time.time()

    print('generating {} hashes with salt: {}'.format(iterations, data))
    hashlist = []
    part = 1  # set this to 1 or 2 change the puzzle part
    for j in range(iterations):
        s = data + str(j)
        m = hashlib.md5(s.encode()).hexdigest()
        if part == 2 and not simple:
            for i in range(2016):
                m = hashlib.md5(m.encode()).hexdigest()
        hashlist.append(m)
    print("time elapsed: {:.2f}".format((time.time() - start_time)))
    start_time = time.time()
    # print('first {}'.format(hashlist[0]))  # part 2: a107ff... part 1: 577571...

    print('search for threes')
    trip = []
    for i in range(len(hashlist)):
        h = hashlist[i]  # seems to be faster to assign to a variable first
        for j in range(len(h) - 2):
            if h[j] == h[j + 1] and h[j] == h[j + 2]:
                trip.append([i, h[j]])
                break
    if verbose > 1:
        print(trip)
    print("time elapsed: {:.2f}".format((time.time() - start_time)))
    start_time = time.time()

    print('search for fives')
    key = []
    while trip:
        idx, h = trip.pop(0)  # yeah, collections.deque is better, but not critical here
        hs = str(h * 5)
        if any(hs in w for w in hashlist[idx + 1:idx + 1000]):
            key.append(idx)
            if verbose > 1:
                print('index found {} in hash {}'.format(idx, hs))

    print('keys found: {}'.format(len(key)))
    if len(key) > 63:
        print('part {}, key at pos 64: {}'.format(part, key[63]))

    print("time elapsed: {:.2f}".format((time.time() - start_time)))


if __name__ == '__main__':
    main()
