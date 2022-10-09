import time


time1 = time.time()
def func():
    input_f = open('input_10.1.txt', 'r')
    input_d = [int(i) for i in input_f.read().split()]
    input_d.sort()
    input_d.insert(0,0)

    steps = []
    for i, item in enumerate(input_d):
        lowest = -4
        for j in range(-3, 0):
            if i + j >= 0:
                if (item - input_d[i+j] >= 1 and item - input_d[i+j] <= 3):
                    lowest = j
                    break
        if lowest > -4:
            steps.append(sum(steps[i+lowest:i]))
        else:
            steps.append(1)

    return steps[-1]


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
