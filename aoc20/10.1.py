import time


time1 = time.time()
def func():
    input_f = open('input_10.1.txt', 'r')
    input_d = [int(i) for i in input_f.read().split()]
    input_d.sort()

    max_j = input_d[-1] + 3
    j_1 = 0
    j_3 = 1
    curr_j = 0
    for i in input_d:
        if i - curr_j == 1:
            j_1 += 1
        if i - curr_j == 3:
            j_3 += 1
        curr_j = i
        if i + 3 == max_j:
            break

    return j_1 * j_3


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
