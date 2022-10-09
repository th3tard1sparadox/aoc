import time

time1 = time.time()
def func():
    input_f = open('input_0.0.txt', 'r')

print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
