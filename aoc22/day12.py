with open("input1.txt") as file:
    inputs = file.readlines()

most = 0
second = 0
third = 0
curr = 0
for l in inputs:
    if l == "\n":
        if curr > most:
            third = second
            second = most
            most = curr
        elif curr > second:
            third = second
            second = curr
        elif curr > third:
            third = curr
        curr = 0
    else:
        curr = curr + int(l)

print(most+second+third)
