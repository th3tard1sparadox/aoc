import time


time1 = time.time()
def func():
    ans = 0

    f = open('input_2.1.txt', 'r')
    for l in f.readlines():
        inputs = l.split()
        c_range = inputs[0].split('-')
        c = inputs[1][:-1]
        if (inputs[2][int(c_range[0]) - 1] == c) != \
           (inputs[2][int(c_range[1]) - 1] == c):
            ans += 1

    return ans


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
