def match_1(s):
    c = 1
    ok = False
    for i in range(1, len(s)):
        a, b = s[i-1:i+1]
        if a > b: return False
        if a == b:
            ok = True
    return ok

def match_2(s):
    c = 1
    ok = False
    for i in range(1, len(s)):
        a, b = s[i-1:i+1]
        if a > b: return False
        if a == b:
            c += 1
        elif c == 2:
            ok = True
            c = 1
        else:
            c = 1
    if c == 2 or ok: return True
    return False

f = open('data/input4.txt', 'r')
a, b = [int(i) for i in f.read().split('-')]

s = 0
for i in range(a, b+1):
    c = str(i)
    if match_1(c): s += 1

print(s)