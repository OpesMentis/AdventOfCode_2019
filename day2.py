def f(l):
  i,p=0,l[0]
  while p<3:a,b,c=l[i+1:i+4];l[c],i=[l[a]+l[b],l[a]*l[b]][p-1],i+4;p=l[i]
  return l[0]
i=list(map(int,open('data/input2.txt').read().split(',')))
h=100
for x in range(h*h):
  n,v=x//h,x%h;l=i[::];l[1:3]=n,v
  if f(l)==19690720:print(h*n+v)