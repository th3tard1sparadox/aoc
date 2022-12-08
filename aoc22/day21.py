with open("input2.txt") as file:
    inputs = file.readlines()

score = 0
for i in inputs:
    if i[0] == 'A':
        if i[2] == 'X':
            score = score + 1 + 3
        elif i[2] == 'Y':
            score = score + 2 + 6
        elif i[2] == 'Z':
            score = score + 3 + 0
    elif i[0] == 'B':
        if i[2] == 'X':
            score = score + 1 + 0
        elif i[2] == 'Y':
            score = score + 2 + 3
        elif i[2] == 'Z':
            score = score + 3 + 6
    elif i[0] == 'C':
        if i[2] == 'X':
            score = score + 1 + 6
        elif i[2] == 'Y':
            score = score + 2 + 0
        elif i[2] == 'Z':
            score = score + 3 + 3

print(score)
