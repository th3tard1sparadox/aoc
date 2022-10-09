import time
import copy


time1 = time.time()
def func():
    input_f = open('input_11.1.txt', 'r')
    input_d = [[j for j in i if j != '\n'] for i in input_f.readlines()]

    def find_next(x, y, direction):
        i = x
        j = y
        while j >= 0 and direction == 0:
            if input_d[j][i] != '.' and j != y:
                return input_d[j][i]
            j -= 1
        while j >= 0 and i < len(input_d[0]) and direction == 1:
            if input_d[j][i] != '.' and j != y and i != x:
                return input_d[j][i]
            j -= 1
            i += 1
        while i < len(input_d[0]) and direction == 2:
            if input_d[j][i] != '.' and i != x:
                return input_d[j][i]
            i += 1
        while j < len(input_d) and i < len(input_d[0]) and direction == 3:
            if input_d[j][i] != '.' and j != y and i != x:
                return input_d[j][i]
            j += 1
            i += 1
        while j < len(input_d) and direction == 4:
            if input_d[j][i] != '.' and j != y:
                return input_d[j][i]
            j += 1
        while i >= 0 and j < len(input_d) and direction == 5:
            if input_d[j][i] != '.' and j != y and i != x:
                return input_d[j][i]
            i -= 1
            j += 1
        while i >= 0 and direction == 6:
            if input_d[j][i] != '.' and i != x:
                return input_d[j][i]
            i -= 1
        while i >= 0 and j >= 0 and direction == 7:
            if input_d[j][i] != '.' and j != y and i != x:
                return input_d[j][i]
            i -= 1
            j -= 1

        return '.'

    def neighbours(x, y):
        nei = []
        
        for i in range(8):
            val = find_next(x, y, i)
            if val != '.':
                nei.append(val)
        return nei

    identical = False
    new_state = copy.deepcopy(input_d)
    while not identical:
        for y in range(len(input_d)):
            for x in range(len(input_d[0])):
                if input_d[y][x] == 'L':
                    if not '#' in neighbours(x, y):
                        new_state[y][x] = '#'
                                
                elif input_d[y][x] == '#':
                    if neighbours(x, y).count('#') >= 5:
                        new_state[y][x] = 'L'

        if new_state == input_d:
            identical = True
        else:
            input_d = copy.deepcopy(new_state)

    count = 0
    for i in range(len(input_d)):
        count += input_d[i].count('#')
    return(count)


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
