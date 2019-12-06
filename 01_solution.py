import time
simple = False

start_time = time.time()

if simple:
    data = "100756".splitlines()
else:
    file = open("01_input.txt", "r")
    data = file.read().splitlines()

fuel = 0
for line in data:
    fuel += int(int(line)/3) - 2

print("first required: %i" % fuel)

middle_time = time.time()
print("time elapsed: %s" % (middle_time - start_time))

total = 0
for line in data:
    fuel = int(int(line) / 3) - 2
    extra = fuel
    for i in range(11):
        extra = max(int(int(extra)/3) - 2, 0)
        fuel += extra
    total += fuel

print("second required: %i" % total)

end_time = time.time()
print("time elapsed: %s" % (end_time - middle_time))
