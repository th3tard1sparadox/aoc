from copy import deepcopy

with open("input11.txt") as file:
    inputs = file.readlines()

grid = [[int(el) for el in row if not el == '\n'] for row in inputs]


def print_grid(grid):
    for row in grid:
        for el in row:
            print(el, end='')
        print()
    print()


def get_neighbours(pos):
    neighbours = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if pos[0]+x >= 0 and pos[0]+x < len(grid[0]) and\
               pos[1]+y >= 0 and pos[1]+y < len(grid):
                if x != 0 or y != 0:
                    neighbours.append((pos[0]+x, pos[1]+y))
    return neighbours


def step(grid):
    flashes = 0
    is_flashing = [[False for el in row] for row in grid]
    new_state = deepcopy(grid)
    for y, row in enumerate(grid):
        for x in range(len(row)):
            new_state[y][x] += 1
            if new_state[y][x] == 10:
                is_flashing[y][x] = True
                flashes += 1

    flashing = True
    while flashing:
        flashing = False
        for y, row in enumerate(grid):
            for x in range(len(row)):
                if is_flashing[y][x]:
                    neighbours = get_neighbours((x,y))
                    for nx, ny in neighbours:
                        new_state[ny][nx] += 1
                        if new_state[ny][nx] == 10:
                            is_flashing[ny][nx] = True
                            flashing = True
                            flashes += 1
                    is_flashing[y][x] = False


    for y, row in enumerate(grid):
        for x in range(len(row)):
            if new_state[y][x] > 9:
                new_state[y][x] = 0

    return new_state, flashes


def do_steps(grid, steps):
    flashes = 0
    for n in range(steps):
        grid, s = step(grid)
        flashes += s
    return flashes


# print(do_steps(grid, 100))


def step2(grid):
    flashes = 0
    is_flashing = [[False for el in row] for row in grid]
    new_state = deepcopy(grid)
    for y, row in enumerate(grid):
        for x in range(len(row)):
            new_state[y][x] += 1
            if new_state[y][x] == 10:
                is_flashing[y][x] = True
                flashes += 1

    flashing = True
    while flashing:
        flashing = False
        for y, row in enumerate(grid):
            for x in range(len(row)):
                if is_flashing[y][x]:
                    neighbours = get_neighbours((x,y))
                    for nx, ny in neighbours:
                        new_state[ny][nx] += 1
                        if new_state[ny][nx] == 10:
                            is_flashing[ny][nx] = True
                            flashing = True
                            flashes += 1
                    is_flashing[y][x] = False


    for y, row in enumerate(grid):
        for x in range(len(row)):
            if new_state[y][x] > 9:
                new_state[y][x] = 0

    return new_state, flashes == len(grid) * len(grid[0])


def do_many_steps(grid):
    i = 0
    while True:
        grid, s = step2(grid)
        i += 1
        if s:
            return i

print(do_many_steps(grid))
