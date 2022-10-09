import time


time1 = time.time()
def func():
    input_f = open('input_9.1.txt', 'r')
    input_d = [int(i) for i in input_f.read().split()]

    ran = []
    stop = False
    for i, num1 in enumerate(input_d):
        for j, num2 in enumerate(input_d[i:]):
            if sum(input_d[i:j+1]) == 217430975:
                ran = input_d[i:j+1]
                stop = True
                break
        if stop:
            break

    ran.sort()
    return ran[0] + ran[-1]


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
