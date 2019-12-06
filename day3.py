def analyse_ligne(inst, curr, d):
    sens=inst[0]
    i,j=curr
    lg=int(inst[1:])
    if sens=='U': v=[[i-lg, i], j, 0, 0]; i-=lg
    if sens=='D': v=[[i, i+lg], j, 0, 1]; i+=lg
    if sens=='L': v=[i, [j-lg, j], 1, 0]; j-=lg
    if sens=='R': v=[i, [j, j+lg], 1, 1]; j+=lg
    return v+[d+lg],[i,j],d+lg

def cross_ligne(l1, l2):
    if l1[2]==l2[2]:return False
    if l1[2]==0:
        if l1[0][0]<=l2[0]<=l1[0][1]and l2[1][0]<=l1[1]<=l2[1][1]:
            return [l2[0], l1[1]]
    if l2[2]==0:
        if l1[1][0]<=l2[1]<=l1[1][1]and l2[0][0]<=l1[0]<=l2[0][1]:
            return [l1[0], l2[1]]
    return False

def pt_in_ligne(pt, ligne):
    if ligne[2]==0 and ligne[1]==pt[1] and ligne[0][0]<=pt[0]<=ligne[0][1]:
        return True
    if ligne[2]==1 and ligne[0]==pt[0] and ligne[1][0]<=pt[1]<=ligne[1][1]:
        return True
    return False

def calc_lg(pt, ligne):
    d = ligne[3]
    o = ligne[2]
    return ligne[4] - abs(ligne[o][d] - pt[o])

man_dist=lambda v:abs(v[0])+abs(v[1])

trajet=[i[:-1].split(',')for i in open('data/input3.txt').readlines()]
lignes_1 = []
curr=[0,0]
d=0
for i in trajet[0]:
    v, curr, d = analyse_ligne(i, curr, d)
    lignes_1 += [v]

d1 = 10**5
d2 = 10**5
lignes_2 = []
curr=[0,0]
d = 0
for i in trajet[1]:
    v, curr, d = analyse_ligne(i, curr, d)
    lignes_2 += [v]
    for l in lignes_1:
        point=cross_ligne(l,v)
        if point and point!=[0,0]:
            d1 = min(d1, man_dist(point))
            d_step1 = calc_lg(point, l)
            d_step2 = calc_lg(point, v)
            d2 = min(d_step1+d_step2, d2)
print(d1)
print(d2)