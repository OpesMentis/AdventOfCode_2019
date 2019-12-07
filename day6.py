data = open('data/input6.txt', 'r')
orbs = data.readlines()

d = {}

for orb in orbs:
    c1 = orb[:3]
    c2 = orb[4:7]

    d[c2] = c1

s = 0

for p in d:
    curr_p = p
    while curr_p in d:
        curr_p = d[curr_p]
        s += 1

print(s)