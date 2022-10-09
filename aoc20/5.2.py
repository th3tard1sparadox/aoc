import time


time1 = time.time()
def func():
    input_f = open('input_5.1.txt', 'r')
    input_d = [i for i in input_f.read().split()]

    highest = 0
    seats = []
    for seat in input_d:
        row = int(seat[:7].replace('F', '0').replace('B', '1'), 2)
        column = int(seat[7:].replace('L', '0').replace('R', '1'), 2)
        ID = row * 8 + column
        seats.append(ID)

    print(seats)
    for i in range(858):
        if (not i in seats) and \
           (i + 1 in seats) and \
           (i - 1 in seats):
            return i   


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
