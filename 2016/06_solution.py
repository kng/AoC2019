# --- Day 6: Signals and Noise ---
# https://adventofcode.com/2016/day/6

import string
import time
simple = False
verbose = 1

if simple:
    data = ['eedadn', 'drvtee', 'eandsr', 'raavrd',
            'atevrs', 'tsrnev', 'sdttsa', 'rasrtv',
            'nssdts', 'ntnada', 'svetve', 'tesnvt',
            'vntsnd', 'vrdear', 'dvrsen', 'enarar']
    dl = 6
else:
    file = open('06_input.txt', 'r')
    data = file.read().splitlines()
    dl = 8


def main():
    start_time = time.time()

    freq = [{a: 0 for a in list(string.ascii_lowercase)} for _ in range(dl)]
    # list of dict in the form of {'a': 0, 'b': 0, ... }
    # access example freq[5]['p'] += 2

    if verbose > 1:
        print('data:\n{}'.format(data))

    # part 1 and 2
    for row in data:
        for i in range(dl):
            freq[i][row[i]] += 1

    msg1 = []
    msg2 = []
    for i in range(dl):
        if verbose > 1:
            print(freq[i])
        msg1 += [k for k, v in freq[i].items() if v == max(freq[i].values())]
        msg2 += [k for k, v in freq[i].items() if v == max(min(freq[i].values()), 1)]
    print('part 1: {}'.format(''.join(msg1)))
    print('part 2: {}'.format(''.join(msg2)))

    middle_time = time.time()
    print("part 1 time elapsed: {} seconds".format(middle_time - start_time))
    end_time = time.time()
    print("part 2 time elapsed: {} seconds".format(end_time - middle_time))


if __name__ == '__main__':
    main()