def intcode(code, inp):
    i = 0
    idx_inp = 0
    ruban = code[:]
    op = ruban[i]
    off = 0
    output = []

    while True:
        inst = op % 100
        mode = str(op // 100)[::-1]+'000'

        if inst in [1, 2, 5, 6, 7, 8, 9]:
            a = ruban[i+1]
            if mode[0] in '02' and a+off >= len(ruban):
                ruban += [0] * (a+off-len(ruban)+1)
            if mode[0] == '0':
                a = ruban[a]
            if mode[0] == '2':
                a = ruban[a+off]
        if inst in [1, 2, 5, 6, 7, 8]:
            b = ruban[i+2]
            if mode[1] in '02' and b+off >= len(ruban):
                ruban += [0] * (b+off-len(ruban)+1)
            if mode[1] == '0':
                b = ruban[b]
            if mode[1] == '2':
                b = ruban[b+off]
        if inst in [1, 2, 7, 8]:
            c = ruban[i+3]
            if mode[2] == '0' and c >= len(ruban):
                ruban += [0] * (c-len(ruban)+1)
            elif mode[2] == '2' and c+off >= len(ruban):
                ruban += [0] * (c+off-len(ruban)+1)
            
            if mode[2] == '2':
                c += off

        if inst == 1:
            ruban[c] = a+b
            i += 4
        elif inst == 2:
            ruban[c] = a*b
            i += 4

        elif inst == 3:
            r = ruban[i+1]
            if r+off >= len(ruban):
                ruban += [0] * (r+off-len(ruban)+1)
            if mode[0] == '0':
                ruban[r] = inp[idx_inp]
            if mode[0] == '2':
                ruban[r+off] = inp[idx_inp]
            idx_inp += 1
            i += 2
        elif inst == 4:
            r = ruban[i+1]
            if mode[0] in '02' and r+off >= len(ruban):
                ruban += [0] * (r+off-len(ruban)+1)
            if mode[0] == '0':
                r = ruban[r]
            if mode[0] == '2':
                r = ruban[r+off]
            output += [r]
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
            return output
        op = ruban[i]

def str2int(data):
    l = []
    for i in data:
        l += [ord(i)]
    return l

with open('data/input17.txt') as data:
    code = [int(i) for i in data.read().split(',')]

res = intcode(code, [])
grid = ['']

for i in res:
    if i == 10:
        grid += ['']
    else:
        grid[-1] += chr(i)

grid = grid[:-2]

c = 0
for i in range(1, len(grid)-1):
    for j in range(1, len(grid[i])-1):  
        if (grid[i][j] == '#' and 
            grid[i-1][j] == '#' and 
            grid[i+1][j] == '#' and 
            grid[i][j-1] == '#' and 
            grid[i][j+1] == '#'):
            c += i*j
        if grid[i][j] in '<>^v':
            pos_i = i
            pos_j = j

print(c)

# The following has been found by hand...
routine = 'A,B,A,C,B,C,B,A,C,B\n'
funct_a = 'L,10,L,6,R,10\n'
funct_b = 'R,6,R,8,R,8,L,6,R,8\n'
funct_c = 'L,10,R,8,R,8,L,10\n'
livefeed = 'n\n'

inp = str2int(routine+funct_a+funct_b+funct_c+livefeed)

code[0] = 2
print(intcode(code, inp)[-1])