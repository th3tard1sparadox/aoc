with open("input2.txt") as file:
    inputs = file.readlines()

steps = [[i.split()[0], int(i.split()[1])] for i in inputs]

def cal_pos(steps):
    dep = 0
    hor = 0

    for i in steps:
        if i[0] == "forward":
            hor = hor + i[1]
        elif i[0] == "down":
            dep = dep + i[1]
        elif i[0] == "up":
            dep = dep - i[1]

    return dep * hor

print("problem 1:" + str(cal_pos(steps)))

def cal_pos2(steps):
    dep = 0
    hor = 0
    aim = 0

    for i in steps:
        if i[0] == "forward":
            hor = hor + i[1]
            dep = dep + aim * i[1]
        elif i[0] == "down":
            aim = aim + i[1]
        elif i[0] == "up":
            aim = aim - i[1]

    return dep * hor

print("problem 2:" + str(cal_pos2(steps)))
