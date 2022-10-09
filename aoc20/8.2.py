import time


time1 = time.time()
def func():
    input_f = open('input_8.1.txt', 'r')
    prog = input_f.readlines()

    def exec(prog):    
        been_to = tuple()
        i = 0
        acc = 0
        while not i in been_to:
            if i < 0 or i >= len(prog):
                return acc
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
                
        return 0

    for i, l in enumerate(prog):
        if l.split()[0] == 'nop':
            res = exec(prog[:i] + ['jmp ' + prog[i].split()[1]] + prog[i+1:])
            if res != 0:
                return res

        if l.split()[0] == 'jmp':
            res = exec(prog[:i] + ['nop ' + prog[i].split()[1]] + prog[i+1:])
            if res != 0:
                return res


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
