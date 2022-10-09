import time
import copy


time1 = time.time()
def func():
    input_f = open('input_11.1.txt', 'r')
    input_d = [[j for j in i if j != '\n'] for i in input_f.readlines()]

    identical = False
    new_state = copy.deepcopy(input_d)
    while not identical:
        for y in range(len(input_d)):
            for x in range(len(input_d[0])):
                if input_d[y][x] == 'L':
                    found_occ = False
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            if (dy != 0 or dx != 0) and (y+dy >= 0 and x+dx >= 0 and y+dy < len(input_d) and x+dx < len(input_d[0]) and input_d[y+dy][x+dx] == '#'):
                                found_occ = True
                                break
                        if found_occ:
                            break
                    if not found_occ:
                        new_state[y][x] = '#'
                                
                elif input_d[y][x] == '#':
                    count = 0
                    for dy in range(-1, 2):
                        for dx in range(-1, 2):
                            if (dy != 0 or dx != 0) and (y+dy >= 0 and x+dx >= 0 and y+dy < len(input_d) and x+dx < len(input_d[0]) and input_d[y+dy][x+dx] == '#'):
                                count += 1
                                if count >= 4:
                                    break
                        if count >= 4:
                            break
                    if count >= 4:
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
