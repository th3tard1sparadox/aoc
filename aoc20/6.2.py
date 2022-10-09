import time


time1 = time.time()
def func():
    input_f = open('input_6.1.txt', 'r')
    input_d = input_f.readlines()
    input_d.append('\n')
    
    summ = 0
    common = set()
    first = True
    for l in input_d:
        if l == '\n':
            summ += len(common)
            common = set()
            first = True
        else:
            if first:
                first = False
                for c in l:
                    if  c != '\n':
                        common.add(c)
            else:
                common_temp = set()
                for c in l:
                    if c in common:
                        common_temp.add(c)
                common = common_temp
    
    return summ


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
