import time


time1 = time.time()
def func():
    input_f = open('input_9.1.txt', 'r')
    input_d = [int(i) for i in input_f.read().split()]

    found = False
    i = 0
    while not found:
        found = True
        for j, num1 in enumerate(input_d[i:i+25]):
            for k, num2 in enumerate(input_d[i:i+25]):
                if num1 + num2 == input_d[i+25] and j != k:
                    found = False
                    break
            if not found:
                break

        i += 1

    return input_d[i+24]


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
