# read input into a matrix
terrain = open("input.txt", "r").read().splitlines()

# movement
right = 3
down = 1

x = 0
y = 0
hit = 0
# y increases by 1 until it hits the bottom
# x increases until it hits the right side, then it resets to 0

while y < len(terrain):
    if terrain[y][x] == '#':
        hit +=1
    x = (x + right) % (len(terrain[0]))
    y += down
print(hit)