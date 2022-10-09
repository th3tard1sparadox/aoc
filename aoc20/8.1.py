import time


time1 = time.time()
def func():
    input_f = open('input_8.1.txt', 'r')
    prog = input_f.readlines()
    
    been_to = tuple()
    i = 0
    acc = 0
    while not i in been_to:
        been_to += (i,)
        l = prog[i]
        ins = l.split()
        if ins[0] == 'jmp':
            if ins[1][0] == '+':
                i += int(ins[1][1:]) - 1
            else:
                i -= int(ins[1][1:]) + 1
        elif ins[0] == 'acc':
            if ins[1][0] == '+':
                acc += int(ins[1][1:])
            else:
                acc -= int(ins[1][1:])
        i += 1
            
    return acc


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
