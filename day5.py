def intcode(code, inp):
    i = 0
    output = []
    ruban = code[::]
    op = ruban[0]
    while op % 100 != 99:
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
        if inst == 2:
            a = ruban[i+1]
            if mode[0] == '0': a = ruban[a]
            b = ruban[i+2]
            if mode[1] == '0': b = ruban[b]
            r = ruban[i+3]
            ruban[r] = a*b
            i += 4
        if inst == 3:
            r = ruban[i+1]
            ruban[r] = inp
            i += 2
        if inst == 4:
            r = ruban[i+1]
            if mode[0] == '0': r = ruban[r]
            output += [r]
            i += 2
        if inst == 5:
            a = ruban[i+1]
            if mode[0] == '0': a = ruban[a]
            r = ruban[i+2]
            if mode[1] == '0': r = ruban[r]
            i = r if a != 0 else i+3
        if inst == 6:
            a = ruban[i+1]
            if mode[0] == '0': a = ruban[a]
            r = ruban[i+2]
            if mode[1] == '0': r = ruban[r]
            i = r if a == 0 else i+3
        if inst == 7:
            a = ruban[i+1]
            if mode[0] == '0': a = ruban[a]
            b = ruban[i+2]
            if mode[1] == '0': b = ruban[b]
            r = ruban[i+3]
            ruban[r] = int(a < b)
            i += 4
        if inst == 8:
            a = ruban[i+1]
            if mode[0] == '0': a = ruban[a]
            b = ruban[i+2]
            if mode[1] == '0': b = ruban[b]
            r = ruban[i+3]
            ruban[r] = int(a == b)
            i += 4
        if inst == 99:
            break
        op = ruban[i]

    return output

data = open('data/input5.txt', 'r')
code = [int(i) for i in data.read().split(',')]

print('Part 1:', intcode(code, 1))
print('Part 2:', intcode(code, 5))