# --- Day 5: Alchemical Reduction ---
# https://adventofcode.com/2018/day/5

import time
simple = False

start_time = time.time()

if simple:
    data = "dabAcCaCBAcCcaDA"
else:
    file = open("05_input.txt", "r")
    data = file.read().strip()

d = list(data)

i = 0
j = 0
while True:
    dl = len(d) - 2
    if i > dl:
        if j == 0:
            break
        else:
            i = 0
            j = 0
    if d[i].lower() == d[i+1].lower() and d[i] != d[i+1]:
        j = 1
        del(d[i:i+2])
        if i > 1:
            i -= 1
    else:
        i += 1

print("eliminated length: %i" % len(d))

middle_time = time.time()
print("time elapsed: %s" % (middle_time - start_time))

ar = 'abcdefghijklmnopqrstuvwxyz'
minimal = len(d)
minimal_a = 'a'

for a in ar:
    db = []
    for i in range(0, len(d)):
        if d[i].lower() != a:
            db.append(d[i])
    i = 0
    j = 0
    while True:
        dl = len(db) - 2
        if i > dl:
            if j == 0:
                if dl < minimal:
                    minimal = dl + 2
                    minimal_a = a
                break
            else:
                i = 0
                j = 0

        if db[i].lower() == db[i+1].lower() and db[i] != db[i+1]:
            j = 1
            del(db[i:i+2])
            if i > 1:
                i -= 1
        else:
            i += 1

print("shortest when excluding '%c' is: %i" % (minimal_a, minimal))
end_time = time.time()
print("time elapsed: %s" % (end_time - middle_time))
