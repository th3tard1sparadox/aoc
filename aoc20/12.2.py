import time
import math


time1 = time.time()
def func():
    input_f = open('input_12.1.txt', 'r')
    input_d = [i for i in input_f.read().split()]

    pos = [0,0]
    wpos = [10,1]
    ang = math.atan2(1, 10)
    for i in input_d:
        if i[0] == 'N':
            wpos[1] += int(i[1:])
            ang = math.atan2(wpos[1], wpos[0])
        elif i[0] == 'S':
            wpos[1] -= int(i[1:])
            ang = math.atan2(wpos[1], wpos[0])
        elif i[0] == 'E':
            wpos[0] += int(i[1:])
            ang = math.atan2(wpos[1], wpos[0])
        elif i[0] == 'W':
            wpos[0] -= int(i[1:])
            ang = math.atan2(wpos[1], wpos[0])

        elif i[0] == 'L':
            ang += ((int(i[1:]) * math.pi) / 180)
            ang = ang % (2 * math.pi)
            l = math.sqrt(math.pow(abs(wpos[0]), 2) + math.pow(abs(wpos[1]), 2))
            wpos[0] = l * math.cos(ang)
            wpos[1] = l * math.sin(ang)
        elif i[0] == 'R':
            ang -= ((int(i[1:]) * math.pi) / 180)
            ang = ang % (2 * math.pi)
            l = math.sqrt(math.pow(abs(wpos[0]), 2) + math.pow(abs(wpos[1]), 2))
            wpos[0] = l * math.cos(ang)
            wpos[1] = l * math.sin(ang)
        elif i[0] == 'F':
            pos[0] += wpos[0] * int(i[1:])
            pos[1] += wpos[1] * int(i[1:])

    return math.fabs(pos[0]) + math.fabs(pos[1])


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
