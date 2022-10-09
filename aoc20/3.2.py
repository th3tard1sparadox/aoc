import time


time1 = time.time()
def func(x, y):
    input_f = open('input_3.1.txt', 'r')
    input_d = input_f.readlines()

    trees = 0
    for i, l in enumerate(input_d):
        if l[(i // y * x) % (len(l) - 1)] == '#' and i % y == 0:
            trees += 1
    return trees


print(func(1,1) * func(3,1) * func(5,1) * func(7,1) * func(1,2))
print("time: " + str((time.time() - time1) * 1000) + "ms")
