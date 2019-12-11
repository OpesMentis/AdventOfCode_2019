import math

def calc_angle(a, b):
    if a >= 0 and b > 0:
        return math.atan(a/b)
    if a > 0 and b <= 0:
        return math.atan(-b/a) + math.pi/2
    if a <= 0 and b < 0:
        return math.atan(a/b) + math.pi
    if a < 0 and b >= 0:
        return math.atan(-b/a) + 3*math.pi/2

with open('data/input10.txt') as data:
    stations = [list(i[:-1]) for i in data.readlines()]

x = len(stations)   
y = len(stations[0])

max_tot = 0

for i in range(x):
    for j in range(y):

        if stations[i][j] != '#':
            continue

        st = [i[:] for i in stations]
        st[i][j] = '.'
        k = min(y-1, j+1)
        while k<y and st[i][k] == '.':
            k += 1
        st[i][k+1:] = ['.'] * (y-k-1)
        k = max(0, j-1)
        while k>0 and st[i][k] == '.':
            k -= 1
        st[i][:k] = ['.'] * k

        for k in range(i-1, -1, -1):
            l = st[k]
            for p in range(y):
                if l[p] == '#':
                    ex = k-i
                    ey = p-j
                    r = math.gcd(ex, ey)
                    ex1, ey1 = ex//r, ey//r
                    c = r+1
                    while 0 <= j+c*ey1 < y and 0 <= i+c*ex1 < x:
                        st[i+c*ex1][j+c*ey1] = '.'
                        c += 1

        for k in range(i+1, x):
            l = st[k]
            for p in range(y):
                if l[p] == '#':
                    ex = k-i
                    ey = p-j
                    r = math.gcd(ex, ey)
                    ex1, ey1 = ex//r, ey//r
                    c = r+1
                    while 0 <= j+c*ey1 < y and 0 <= i+c*ex1 < x:
                        st[i+c*ex1][j+c*ey1] = '.'
                        c += 1

        tot = sum(i.count('#') for i in st)
        if tot > max_tot:
            max_tot = tot
            map_ast = st
            st_x = i
            st_y = j

print(max_tot)

d_ast = []

for i in range(x):
    for j in range(y):
        if map_ast[i][j] == '#':
            di = st_x - i
            dj = j - st_y
            ang = calc_angle(dj, di)

            d_ast += [[(i, j), ang]]

res = sorted(d_ast, key=lambda i: i[1])
a_200 = res[199][0]

print(a_200[1]*100+a_200[0])