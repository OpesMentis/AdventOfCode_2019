d=open('data/input2.txt', 'r')
s=d.read().split(',')
l=[int(i)for i in s]
l[1:3]=[12,2]
i=0
p=l[0]
while p<3:
    a=l[l[i+1]]
    b=l[l[i+2]]
    c=l[i+3]
    if p==1:
        l[c]=a+b
    elif p==2:
        l[c]=a*b
    i+=4
    p=l[i]

print(l[0])

def f(l):
    i,p=0,l[0]
    while p<3:
        a,b,c=l[i+1:i+4]
        l[c]=[l[a]+l[b],l[a]*l[b]][p-1]
        i+=4
        p=l[i]
    return l[0]

i=list(map(int,s))
h=100
for x in range(h*h):
    n,v=x//h,x%h
    l=i[::]
    l[1:3]=n,v
    if f(l)==19690720:
        print(h*n+v)
        break

d.close()