x, y, hit = 0, 0, 0

for row in open("input.txt", "r").read().splitlines():
    if row[x] == '#':
        hit +=1
    x = (x + 3) % len(row)
    y += 1
print(hit)