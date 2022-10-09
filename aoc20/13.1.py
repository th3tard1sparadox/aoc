import time
from math import ceil
from math import inf


time1 = time.time()
def func():
    input_f = open('input_13.1.txt', 'r')
    input_d = input_f.readlines()

    t = int(input_d[0][:-1])
    busses = input_d[1].split(',')

    lowest = inf
    lowest_b = 0
    for b in busses:
        if b != 'x':
            if ceil(t/int(b)) * int(b) - t < lowest:
                lowest = ceil(t/int(b)) * int(b) - t
                lowest_b = int(b)

    return(lowest * lowest_b)
    

print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
