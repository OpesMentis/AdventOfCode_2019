def intcode(code):
    i = 0
    ruban = code[:]
    op = ruban[i]
    off = 0
    output = []
    c_out = 0
    score = 0

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

            if ball_x > padl_x:
                inp = 1
            elif ball_x < padl_x:
                inp = -1
            else:
                inp = 0

            if mode[0] == '0': ruban[r] = inp
            if mode[0] == '2': ruban[r+off] = inp
            i += 2
        elif inst == 4:
            r = ruban[i+1]
            if mode[0] in '02' and r+off >= len(ruban): ruban += [0] * (r+off-len(ruban)+1)
            if mode[0] == '0': r = ruban[r]
            if mode[0] == '2': r = ruban[r+off]
            output += [r]
            c_out += 1
            if c_out % 3 == 0:
                if output[-1] == 4:
                    ball_x = output[-3]
                elif output[-1] == 3:
                    padl_x = output[-3]
                if output[-3] == -1 and output[-2] == 0:
                    score = output[-1]
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
            return output, score
        op = ruban[i]

with open('data/input13.txt') as data:
    code = [int(i) for i in data.read().split(',')]

out, _ = intcode(code[:])

s_blocks = 0
i = 2
while i < len(out):
    s_blocks += int(out[i] == 2)
    i += 3

print(s_blocks)

code[0] = 2
_, score = intcode(code[:])
print(score)