def p_level(x, y, s_nr):
    return int(str((((x + 10) * y) + s_nr) * (x + 10))[-3]) - 5

def calc(xs, ys, size, grid):
    levels = []
    for i in range(size):
        for j in range(size):
            levels.append(grid[i + xs][j + ys])
    return sum(levels)

def func(s_nr):
    highest = 0
    x = 0
    y = 0
    largest_size = 0
    power_grid = [[p_level(i, j, s_nr) for j in range(300)] for i in range(300)]
    
    for size in range(30):
        print(size)
        for i in range(300 - size):
            for j in range(300 - size):
                if highest < calc(i, j, size, power_grid):
                    highest = calc(i, j, size, power_grid)
                    x = i
                    y = j
                    largest_size = size
    return x, y, largest_size
