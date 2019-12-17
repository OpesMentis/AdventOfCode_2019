with open('data/input16.txt') as f:
    inp = f.read()[:-1]

# phase 1

inp1 = inp
for i in range(100):
    nbs = [int(i) for i in inp1]
    l = len(nbs)
    inp1 = ''
    c = 1
    while c <= l:
        j = c-1
        dig = 0
        l = len(nbs)
        while j < l:
            dig += sum(nbs[j:min(j+c,l)])
            j += 2*c
            dig -= sum(nbs[j:min(j+c,l)])
            j += 2*c

        inp1 += str(dig)[-1]
        c += 1

print(inp1[:8])

# phase 2

offset = int(inp[:7])
inp2 = (inp * 10000)[offset:]
l = len(inp2)
nbs = [int(k) for k in inp2]

for i in range(100):
    p = 0
    for j in range(l-1, -1, -1):
        p += nbs[j]
        nbs[j] = p%10

print(''.join([str(i) for i in nbs[:8]]))