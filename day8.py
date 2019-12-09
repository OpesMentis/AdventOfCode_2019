from PIL import Image

with open('data/input8.txt') as data:
    img = data.read()[:-1]

min_0 = 1000

RED = (255, 0, 0)
BLK = (0, 0, 0)
WHT = (255, 255, 255)
couls = [BLK, WHT, RED]

res = Image.new('RGB', (25, 6), (255, 0, 0))
pxl = res.load()

for i in range(100):
    inf = i*150
    sup = inf+150
    layer = img[inf:sup]

    n0 = layer.count('0')
    n1 = layer.count('1')
    n2 = layer.count('2')

    if n0 < min_0:
        min_0 = n0
        prod = n1 * n2

    for j in range(150):
        col = j % 25
        row = j // 25

        x = int(layer[j])
        if pxl[col, row] == RED:
            pxl[col, row] = couls[x]

print(prod)
res.show()