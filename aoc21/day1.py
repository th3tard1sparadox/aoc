with open("input1.txt") as file:
    inputs = file.readlines()

measurements = [int(i) for i in inputs]

def compare(m):
    increases = 0
    for i in range(len(m)):
        if i > 0 and m[i - 1] < m[i]:
            increases = increases + 1
    return increases

print("problem 1:" + str(compare(measurements)))

sum_measurements = [measurements[i] + measurements[i + 1] + measurements[i + 2] for i in range(len(measurements) - 2)]

print("problem 2:" + str(compare(sum_measurements)))
