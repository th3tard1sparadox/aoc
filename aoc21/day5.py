with open("input5.txt") as file:
    inputs = file.readlines()

vents = [[[int(h) for h in j.split(',')] for j in i[:-1].split(' -> ')] for i in inputs]

max_x = 0
max_y = 0
for i in vents:
    for j in i:
        if j[0] > max_x:
            max_x = j[0]
        if j[1] > max_y:
            max_y = j[1]

grid = [[0 for i in range(max_x + 1)] for j in range(max_y + 1)]

def place_orth(vents, grid):
    for v in vents:
        if v[0][0] == v[1][0]:
            if v[0][1] < v[1][1]:
                for y in range(v[0][1], v[1][1] + 1):
                    grid[y][v[0][0]] += 1
            else:
                for y in range(v[1][1], v[0][1] + 1):
                    grid[y][v[0][0]] += 1
        elif v[0][1] == v[1][1]:
            if v[0][0] < v[1][0]:
                for x in range(v[0][0], v[1][0] + 1):
                    grid[v[0][1]][x] += 1
            else:
                for x in range(v[1][0], v[0][0] + 1):
                    grid[v[0][1]][x] += 1

place_orth(vents, grid)

def count(grid):
    overlap = 0
    for y in grid:
        for x in y:
            if x >= 2:
                overlap += 1
    return overlap

print("part 1:" + str(count(grid)))

def place_diag(vents, grid):
    for v in vents:
        if abs(v[0][0] - v[1][0]) == abs(v[0][1] - v[1][1]):

            if v[0][0] < v[1][0] and v[0][1] < v[1][1]:
                for i in range(abs(v[0][0] - v[1][0]) + 1):
                    grid[v[0][1] + i][v[0][0] + i] += 1

            elif v[0][0] < v[1][0] and v[1][1] < v[0][1]:
                for i in range(abs(v[0][0] - v[1][0]) + 1):
                    grid[v[0][1] - i][v[0][0] + i] += 1

            elif v[1][0] < v[0][0] and v[0][1] < v[1][1]:
                for i in range(abs(v[0][0] - v[1][0]) + 1):
                    grid[v[0][1] + i][v[0][0] - i] += 1

            else:
                for i in range(abs(v[0][0] - v[1][0]) + 1):
                    grid[v[0][1] - i][v[0][0] - i] += 1

place_diag(vents, grid)

print("part 2:" + str(count(grid)))
