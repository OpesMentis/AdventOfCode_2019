# Part 1

import itertools

def intcode(code, inp, start=0):
    i = start
    idx_inp = 0
    ruban = code[::]
    op = ruban[i]
    output = 0
    while True:
        inst = op % 100
        mode = str(op // 100)[::-1]+'000'

        if inst == 1:
            a = ruban[i+1]
            if mode[0] == '0': a = ruban[a]
            b = ruban[i+2]
            if mode[1] == '0': b = ruban[b]
            r = ruban[i+3]
            ruban[r] = a+b
            i += 4
        elif inst == 2:
            a = ruban[i+1]
            if mode[0] == '0': a = ruban[a]
            b = ruban[i+2]
            if mode[1] == '0': b = ruban[b]
            r = ruban[i+3]
            ruban[r] = a*b
            i += 4
        elif inst == 3:
            r = ruban[i+1]
            ruban[r] = inp[idx_inp]
            idx_inp += 1
            i += 2
        elif inst == 4:
            r = ruban[i+1]
            if mode[0] == '0': r = ruban[r]
            return r, ruban, i+2
        elif inst == 5:
            a = ruban[i+1]
            if mode[0] == '0': a = ruban[a]
            r = ruban[i+2]
            if mode[1] == '0': r = ruban[r]
            i = r if a != 0 else i+3    
        elif inst == 6:
            a = ruban[i+1]
            if mode[0] == '0': a = ruban[a]
            r = ruban[i+2]
            if mode[1] == '0': r = ruban[r]
            i = r if a == 0 else i+3
        elif inst == 7:
            a = ruban[i+1]
            if mode[0] == '0': a = ruban[a]
            b = ruban[i+2]
            if mode[1] == '0': b = ruban[b]
            r = ruban[i+3]
            ruban[r] = int(a < b)
            i += 4
        elif inst == 8:
            a = ruban[i+1]
            if mode[0] == '0': a = ruban[a]
            b = ruban[i+2]
            if mode[1] == '0': b = ruban[b]
            r = ruban[i+3]
            ruban[r] = int(a == b)
            i += 4
        elif inst == 99:
            return None, ruban, i
        op = ruban[i]

data = open('data/input7.txt', 'r')
code = [int(i) for i in data.read().split(',')]

max_out = 0
done = False

# (Un)comment the following lines according to the problem you want to solve
#l_phs = itertools.permutations([0, 1, 2, 3, 4], 5)
l_phs = itertools.permutations([5, 6, 7, 8, 9], 5)

for phases in l_phs:
    i = 0
    out = 0
    done = False
    ARR = [code[:] for i in range(5)]
    IDX = [0] * 5
    while not done:
        rub = ARR[i%5]
        idx = IDX[i%5]

        params = [phases[i%5], out] if i<5 else [out]
        tmp, ARR[i%5], IDX[i%5] = intcode(rub, params, idx)

        if tmp == None:
            done = True
        else:
            out = tmp
            i += 1

    if out > max_out:
        max_out = out

print(max_out)