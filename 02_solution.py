import time
simple = False
# simple = True

start_time = time.time()

if simple:
    data = "1,9,10,3,2,3,11,0,99,30,40,50"
    # data = "1,0,0,0,99"
else:
    file = open("02_input.txt", "r")
    data = file.read()

noun = 0
verb = 0
i = 0

d = [int(n) for n in data.split(',')]
if simple:
    print(d)
if d[-1] == '\n':
    del(d[-1])
llen = len(d)
d[1] = 12
d[2] = 2

while i < llen:
    op = d[i]
    if op == 1:
        d[d[i + 3]] = d[d[i + 1]] + d[d[i + 2]]
    if op == 2:
        d[d[i + 3]] = d[d[i + 1]] * d[d[i + 2]]
    if op == 99:
        i = llen
    i += 4

if simple:
    print(d)
else:
    print("first result: %i" % d[0])

middle_time = time.time()
print("time elapsed: %s" % (middle_time - start_time))

done = False
while not done:
    noun += 1
    if noun > 99:
        noun = 0
        verb += 1
    if verb > 99:
        done = True
    d = [int(n) for n in data.split(',')]
    if d[-1] == '\n':
        del(d[-1])
    llen = len(d)

    i = 0
    d[1] = noun
    d[2] = verb

    while i < llen:
        op = int(d[i])
        if op == 1:
            d[d[i + 3]] = d[d[i + 1]] + d[d[i + 2]]
        if op == 2:
            d[d[i + 3]] = d[d[i + 1]] * d[d[i + 2]]
        if op == 99:
            i = llen
        i += 4
    if d[0] == 19690720:
        done = True
        # print("noun: %i" % noun)
        # print("verb: %i" % verb)
        print("second result: %i" % (noun * 100 + verb))

end_time = time.time()
print("time elapsed: %s" % (end_time - middle_time))
