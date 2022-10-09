import time


time1 = time.time()
def func():
    input_f = open('input_3.1.txt', 'r')
    input_d = input_f.readlines()

    trees = 0
    for i, l in enumerate(input_d):
        if l[(i * 3) % (len(l) - 1)] == '#':
            trees += 1
    return trees


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
