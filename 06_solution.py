import time
simple = False
start_time = time.time()

if simple:
    data = "COM)B\nB)C\nC)D\nD)E\nE)F\nB)G\nG)H\nD)I\nE)J\nJ)K\nK)L"
else:
    file = open("06_input.txt", "r")
    data = file.read()

data = data.splitlines()
com = "COM"
you = "YOU"
san = "SAN"
currOrbit = com
nextOrbit = []
comOrbit = ""
sumOrbit = 1
yOrbits = []
sOrbits = []
depth = 1

done = False
while not done:
    if simple:
        print("current level " + currOrbit)
    for line in data:
        (a, b) = line.split(')')
        if a == currOrbit:
            nextOrbit.append([b, depth])
            if simple:
                print("next level " + b)
            sumOrbit += depth
    if len(nextOrbit) > 0:
        (currOrbit, depth) = nextOrbit.pop()
    else:
        done = True
    depth += 1

print("sum levels: %i" % (sumOrbit - 1))

middle_time = time.time()
print("time elapsed: %s" % (middle_time - start_time))

if simple:
    exit(0)

done = False
while not done:
    for line in data:
        (a, b) = line.split(')')
        if com in a and you in b:
            done = True
        if you in b:
            yOrbits.append(a)
            you = a
        if san in b:
            sOrbits.append(a)
            san = a

for you in yOrbits:
    for san in sOrbits:
        if san in you:
            print("first common orbit: " + san)
            comOrbit = san
            break
    if len(comOrbit) > 2:
        break

print("orbit changes: " + str(sOrbits.index(comOrbit) + yOrbits.index(comOrbit)))

end_time = time.time()
print("time elapsed: %s" % (end_time - middle_time))
