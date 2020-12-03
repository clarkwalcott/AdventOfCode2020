# write input into a matrix
terrain = open("input.txt", "r").read().splitlines()

# movement (right, down)
slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

total = 1

for right, down in slopes:
    x, y, hit = 0, 0, 0
    while y < len(terrain):
        if terrain[y][x] == '#':
            hit +=1
        x = (x + right) % (len(terrain[0]))
        y += down
    print("Slope:",(right, down), "Trees hit:", hit)
    total *= hit
print("Product:", total)