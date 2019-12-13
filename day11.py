from PIL import Image

with open('data/input11.txt') as data:
    code = [int(i) for i in data.read().split(',')]

i = 0
ruban = code[:]
op = ruban[i]
off = 0

N, W, S, E = 0, 1, 2, 3

axe = N
# Set l_white_cells = [] to get the answer to part 1
l_white_cells = [[0,0]]
pos = [0, 0]
painted_cells = []
n_out = 0

while True:
    inst = op % 100
    mode = str(op // 100)[::-1]+'000'

    if inst in [1, 2, 5, 6, 7, 8, 9]:
        a = ruban[i+1]
        if mode[0] in '02' and a+off >= len(ruban): ruban += [0] * (a+off-len(ruban)+1)
        if mode[0] == '0': a = ruban[a]
        if mode[0] == '2': a = ruban[a+off]
    if inst in [1, 2, 5, 6, 7, 8]:
        b = ruban[i+2]
        if mode[1] in '02' and b+off >= len(ruban): ruban += [0] * (b+off-len(ruban)+1)
        if mode[1] == '0': b = ruban[b]
        if mode[1] == '2': b = ruban[b+off]
    if inst in [1, 2, 7, 8]:
        c = ruban[i+3]
        if mode[2] == '0' and c >= len(ruban): ruban += [0] * (c-len(ruban)+1)
        elif mode[2] == '2' and c+off >= len(ruban): ruban += [0] * (c+off-len(ruban)+1)
        
        if mode[2] == '2': c += off

    if inst == 1:
        ruban[c] = a+b
        i += 4
    elif inst == 2:
        ruban[c] = a*b
        i += 4

    elif inst == 3:
        r = ruban[i+1]
        if r+off >= len(ruban): ruban += [0] * (r+off-len(ruban)+1)

        inp = int(pos in l_white_cells)

        if mode[0] == '0': ruban[r] = inp
        if mode[0] == '2': ruban[r+off] = inp
        i += 2
    elif inst == 4:
        r = ruban[i+1]
        if mode[0] in '02' and r+off >= len(ruban): ruban += [0] * (r+off-len(ruban)+1)
        if mode[0] == '0': r = ruban[r]
        if mode[0] == '2': r = ruban[r+off]
        
        if n_out % 2 == 0:
            if r == 1 and pos not in l_white_cells:
                l_white_cells += [pos[:]]
            elif r == 0 and pos in l_white_cells:
                l_white_cells.remove(pos)
            if pos not in painted_cells:
                painted_cells += [pos[:]]
        else:
            if r == 0:
                axe = (axe+1)%4
            else:
                axe = (axe-1)%4

            if axe == N:
                pos[0] -= 1
            elif axe == W:
                pos[1] -= 1
            elif axe == S:
                pos[0] += 1
            else:
                pos[1] += 1

        n_out += 1

        i += 2

    elif inst == 5:
        i = b if a != 0 else i+3
    elif inst == 6:
        i = b if a == 0 else i+3
    elif inst == 7:
        ruban[c] = int(a < b)
        i += 4
    elif inst == 8:
        ruban[c] = int(a == b)
        i += 4
    elif inst == 9:
        off += a
        i += 2
    elif inst == 99:
        break
    op = ruban[i]

print(len(painted_cells))

height = max(painted_cells, key=lambda c: c[0])[0]
width = max(painted_cells, key=lambda c: c[1])[1]

res = Image.new('RGB', (width+1, height+1), (0, 0, 0))
pxl = res.load()

for c in l_white_cells:
    pxl[c[1], c[0]] = (255, 255, 255)

res.show()