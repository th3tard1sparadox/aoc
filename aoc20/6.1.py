import time


time1 = time.time()
def func():
    input_f = open('input_6.1.txt', 'r')
    input_d = input_f.readlines()
    input_d.append('\n')
    
    summ = 0
    unique = set()
    for l in input_d:
        if l == '\n':
            summ += len(unique)
            unique = set()
        else:
            for c in l:
                if  c != '\n':
                    unique.add(c)
    
    return summ


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
