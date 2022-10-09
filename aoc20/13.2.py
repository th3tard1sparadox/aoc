import time
from math import ceil
from math import inf


time1 = time.time()
def func():
    input_f = open('input_13.1.txt', 'r')
    input_d = input_f.readlines()

    time = int(input_d[0][:-1])
    busses = input_d[1].split(',')

    mult = 1
    t = 0
    for i, b in enumerate(busses):
        if b != 'x':
            while (t + i) % int(b) != 0:
                t += mult
            mult *= int(b)

    return(t)
    

print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
