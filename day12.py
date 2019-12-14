import itertools
import math

def lcm(l):
    if len(l) == 2:
        return l[0]*l[1]//math.gcd(l[0], l[1])
    return lcm([lcm(l[:2])]+l[2:])  

with open('data/input12.txt') as f:
    l = f.readlines()
    x = [[int(k[2:]) for k in i[1:-2].split(', ')] for i in l]

pos = {i: x[i][:] for i in range(4)}
vel = {i: [0,0,0] for i in range(4)}
sat = [0, 1, 2, 3]
periods = [0, 0, 0]
energy = 0
i = 0

while any(t == 0 for t in periods):
    i += 1
    # Applying gravity
    for s1, s2 in itertools.combinations(sat, 2):
        for j in range(3):
            if pos[s1][j] > pos[s2][j]:
                vel[s1][j] -= 1
                vel[s2][j] += 1
            elif pos[s1][j] < pos[s2][j]:
                vel[s1][j] += 1
                vel[s2][j] -= 1

    # Applying velocity
    for s in sat:
        for j in range(3): pos[s][j] += vel[s][j]

    for j in range(3):
        if all(vel[s][j]==0 and pos[s][j]==x[s][j] for s in sat)and periods[j]==0:
            periods[j] = i

    if i == 1000:
        for s in sat:
            pot = sum(abs(p) for p in pos[s])
            kin = sum(abs(v) for v in vel[s])
            tot = pot*kin
            energy += tot
        print('Total energy:', energy)

print('Period:', lcm(periods))