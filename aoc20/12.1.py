import time
import math


time1 = time.time()
def func():
    input_f = open('input_12.1.txt', 'r')
    input_d = [i for i in input_f.read().split()]

    pos = [0,0]
    ang = 0
    for i in input_d:
        if i[0] == 'N':
            pos[1] += int(i[1:])
        elif i[0] == 'S':
            pos[1] -= int(i[1:])
        elif i[0] == 'E':
            pos[0] += int(i[1:])
        elif i[0] == 'W':
            pos[0] -= int(i[1:])
        elif i[0] == 'L':
            ang += ((int(i[1:]) * math.pi) / 180) 
            ang = ang % (2 * math.pi)
        elif i[0] == 'R':
            ang -= ((int(i[1:]) * math.pi) / 180)
            ang = ang % (2 * math.pi)
        elif i[0] == 'F':
            pos[0] += int(i[1:]) * math.cos(ang)
            pos[1] += int(i[1:]) * math.sin(ang)

    return math.fabs(pos[0]) + math.fabs(pos[1])


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
