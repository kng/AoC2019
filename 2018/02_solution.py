# --- Day 2: Inventory Management System ---
# https://adventofcode.com/2018/day/2

file = open("02_input.txt", "r")
data = file.read().splitlines()
twos = 0
threes = 0
rows = 0

for line in data:
    rows += 1
    ll = []
    for i in line:
        c = 0
        for j in line:
            if i == j:
                c += 1
        ll.append(c)

    if 2 in ll:
        twos += 1
    if 3 in ll:
        threes += 1

print('part 1: {}'.format(twos * threes))

best = 0
score = 0
bs = []
for x in range(0, rows):
    for y in range(x + 1, rows):
        score = 0
        u = zip(data[x], data[y])
        for i, j in u:
            if i == j:
                score += 1
        if score >= best:
            best = score
            bs = [data[x], data[y]]
            # print("score: %i" % score)
            # print("%s - %s" % (data[x], data[y]))

print('part 2:')
for i in range(len(bs[0])):
    if bs[0][i] == bs[1][i]:
        print(bs[0][i], end='')
