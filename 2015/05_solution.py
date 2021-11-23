# https://adventofcode.com/2015/day/5
# --- Day 5: Doesn't He Have Intern-Elves For This? ---

import time
simple = False
verbose = 0

if simple:
    # noinspection SpellCheckingInspection
    data = ['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu',
            'dvszwmarrgswjxmb', 'ghjaaa', 'xyxy', 'qjasdfghqj', 'qjhvhtzxzqqjkmpb',
            'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']
else:
    file = open('05_input.txt', 'r')
    data = file.read().splitlines()

vowels = ['a', 'e', 'i', 'o', 'u']
curses = ['ab', 'cd', 'pq', 'xy']


def main():
    start_time = time.time()

    nice = 0
    for word in data:
        v = t = c = 0
        p = ''
        for letter in list(word):
            if letter in vowels:
                v += 1
            if letter == p:
                t += 1
            if p + letter in curses:
                c += 1
            p = letter
        if verbose > 0:
            print('Testing {}: vowels {}, in a row {}, curses {}'.format(word, v, t, c))
        if v >= 3 and t >= 1 and c == 0:
            nice += 1
    print('part 1 nice strings {}'.format(nice))

    middle_time = time.time()
    print("time elapsed: %s" % (middle_time - start_time))

    nice = 0
    for word in data:
        triplet = doublet = 0
        for i in range(len(word)-2):
            if word[i] == word[i+2]:
                triplet += 1
        for i in range(len(word)-3):
            if word[i:i+2] in word[i+2:]:
                doublet += 1
        if doublet > 0 and triplet > 0:
            nice += 1
        if verbose > 0:
            print('testing {}: double {}, triple {}'.format(word, doublet, triplet))
    print('part 2 nice strings {}'.format(nice))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - middle_time))


if __name__ == '__main__':
    main()
