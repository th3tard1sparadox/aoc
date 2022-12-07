with open("input1.txt") as file:
    inputs = file.readlines()

most = 0
curr = 0
for l in inputs:
    if l == "\n":
        if curr > most:
            most = curr
        curr = 0
    else:
        curr = curr + int(l)

print(most)
