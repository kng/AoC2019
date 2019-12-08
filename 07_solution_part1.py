import time
simple = False
verbose = 0  # 0 = quiet, 1 = some info, 2 = lots

if simple:
    # thruster tests, part 1
    # 43210 from 4,3,2,1,0
    # data = "3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0"
    # 54321 from 0,1,2,3,4
    # data = "3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0"
    # 65210 from 1,0,4,3,2
    data = "3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0"
else:
    file = open("07_input.txt", "r")
    data = file.read()


def main():
    start_time = time.time()

    phases = list('01234')
    thrust = 0
    settings = []
    for p in permutation(phases):
        if verbose > 0:
            print(p)
        result = 0
        for ph in p:
            result = computer([result, int(ph)])
        thrust = max(thrust, result)
        if result == thrust:
            settings = p

    print("part 1, max thrust: %i" % thrust)
    print("settings: " + str(settings))

    end_time = time.time()
    print("time elapsed: %s" % (end_time - start_time))


def pad(s):
    o = [int(x) for x in str(s)]
    return o[::-1] + [0] * abs((len(o)-5))


def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        rem = lst[:i] + lst[i + 1:]
        for p in permutation(rem):
            l.append([m] + p)
    return l


def computer(inp):
    d = [int(n) for n in data.split(',')]  # always run the program from scratch
    i = 0
    out = 0
    while i < len(d):
        op = pad(d[i])
        if verbose > 1:
            print("op: " + str(op))
        if op[0] == 1 and op[1] == 0:  # add # # dst
            if op[2] == 0:
                p1 = d[d[i + 1]]
            else:
                p1 = d[i + 1]
            if op[3] == 0:
                p2 = d[d[i + 2]]
            else:
                p2 = d[i + 2]
            d[d[i + 3]] = p1 + p2
            i += 4
        elif op[0] == 2 and op[1] == 0:  # mul # # dst
            if op[2] == 0:
                p1 = d[d[i + 1]]
            else:
                p1 = d[i + 1]
            if op[3] == 0:
                p2 = d[d[i + 2]]
            else:
                p2 = d[i + 2]
            d[d[i + 3]] = p1 * p2
            i += 4
        elif op[0] == 3 and op[1] == 0:  # load # dst
            d[d[i + 1]] = inp.pop()
            if verbose > 0:
                print("load %i" % d[d[i + 1]])
            i += 2
        elif op[0] == 4 and op[1] == 0:  # output src
            out = d[d[i + 1]]
            if verbose > 0:
                print("out %i" % out)
            i += 2
        elif op[0] == 5 and op[1] == 0:  # jump-if-true # pp
            if op[2] == 0:
                p1 = d[d[i + 1]]
            else:
                p1 = d[i + 1]
            if op[3] == 0:
                p2 = d[d[i + 2]]
            else:
                p2 = d[i + 2]
            if p1 != 0:
                i = p2
            else:
                i += 3
        elif op[0] == 6 and op[1] == 0:  # jump-if-false # pp
            if op[2] == 0:
                p1 = d[d[i + 1]]
            else:
                p1 = d[i + 1]
            if op[3] == 0:
                p2 = d[d[i + 2]]
            else:
                p2 = d[i + 2]
            if p1 == 0:
                i = p2
            else:
                i += 3
        elif op[0] == 7 and op[1] == 0:  # less # # dst
            if op[2] == 0:
                p1 = d[d[i + 1]]
            else:
                p1 = d[i + 1]
            if op[3] == 0:
                p2 = d[d[i + 2]]
            else:
                p2 = d[i + 2]
            if p1 < p2:
                d[d[i + 3]] = 1
            else:
                d[d[i + 3]] = 0
            i += 4
        elif op[0] == 8 and op[1] == 0:  # equals # # dst
            if op[2] == 0:
                p1 = d[d[i + 1]]
            else:
                p1 = d[i + 1]
            if op[3] == 0:
                p2 = d[d[i + 2]]
            else:
                p2 = d[i + 2]
            if p1 == p2:
                d[d[i + 3]] = 1
            else:
                d[d[i + 3]] = 0
            i += 4
        elif op[0] == 9 and op[1] == 9:
            if verbose > 0:
                print("end")
            return out
        else:
            i += 1
    print("program ran out!")
    return -1


main()

