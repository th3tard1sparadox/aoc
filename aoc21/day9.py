with open("input9.txt") as file:
    grid = [[int(j) for j in i[:-1]] for i in file.readlines()]


def find_neighbours(pos):
    neighbours = []
    if not pos[0] == 0:
        neighbours.append(grid[pos[1]][pos[0] - 1])
    if not pos[1] == 0:
        neighbours.append(grid[pos[1] - 1][pos[0]])
    if pos[0] < len(grid[0]) - 1:
        neighbours.append(grid[pos[1]][pos[0] + 1])
    if pos[1] < len(grid) - 1:
        neighbours.append(grid[pos[1] + 1][pos[0]])
    return neighbours


def find_dangers():
    danger = 0
    for y, row in enumerate(grid):
        for x, el in enumerate(row):
            if min(find_neighbours([x, y])) > el:
                danger += el + 1
    return danger


print("part 1:" + str(find_dangers()))


def find_neighbours_pos(pos):
    neighbours = []
    if not pos[0] == 0:
        neighbours.append([pos[0] - 1, pos[1]])
    if not pos[1] == 0:
        neighbours.append([pos[0], pos[1] - 1])
    if pos[0] < len(grid[0]) - 1:
        neighbours.append([pos[0] + 1, pos[1]])
    if pos[1] < len(grid) - 1:
        neighbours.append([pos[0], pos[1] + 1])
    return neighbours


def find_lows():
    lows = []
    for y, row in enumerate(grid):
        for x, el in enumerate(row):
            if min(find_neighbours([x, y])) > el:
                lows.append([x, y])
    return lows


def bfs(start):
    queue = [start]
    visited = []

    while queue:
        current = queue.pop()
        neighbours = find_neighbours_pos(current)
        for n in neighbours:
            if n not in visited and not grid[n[1]][n[0]] == 9:
                queue.append(n)
                visited.append(n)

    return len(visited)


def basin_sizes():
    basins = []
    for low in find_lows():
        bas = bfs(low)
        basins.append(bas)

    basins.sort(reverse=True)
    return basins[0] * basins[1] * basins[2]


print("part 2:" + str(basin_sizes()))
