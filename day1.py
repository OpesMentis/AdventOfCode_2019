d=open('data/input1.txt', 'r')
def f(m,s):
    if m>0:
        u=max(0,m//3-2)
        return f(u,s+u)
    return s
l=map(int, d.readlines()[:-1])
print(sum(f(m,0) for m in l))
d.close()