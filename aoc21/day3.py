with open("input3.txt") as file:
    inputs = file.readlines()


def get_gamma(data):
    gamma = ''
    for i in range(len(data[0]) - 1):
        tsum = 0
        for j in range(len(data)):
            tsum = tsum + int(data[j][i])
        if tsum > len(data)/2:
            gamma = gamma + '1'
        else:
            gamma = gamma + '0'
    return gamma


def get_epsilon(gamma):
    epsilon = ''
    for i in range(len(gamma)):
        if gamma[i] == '1':
            epsilon = epsilon + '0'
        else:
            epsilon = epsilon + '1'
    return epsilon


gamma = get_gamma(inputs)
epsilon = get_epsilon(gamma)
print("problem 1:" + str(int(gamma, 2) * int(epsilon, 2)))


def get_ox(data):
    ideal = ''
    temp = data.copy()
    for i in range(len(data[0]) - 1):
        ones = 0
        zeros = 0
        for j in range(len(temp)):
            if temp[j][i] == '1':
                ones = ones + 1
            else:
                zeros = zeros + 1
        if ones >= zeros:
            ideal = ideal + '1'
        else:
            ideal = ideal + '0'

        for j in range(len(data)):
            if (not data[j][i] == ideal[i]) and (data[j] in temp):
                temp.remove(data[j])
                if len(temp) == 1:
                    return temp[0]


def get_co(data):
    ideal = ''
    temp = data.copy()
    for i in range(len(data[0]) - 1):
        ones = 0
        zeros = 0
        for j in range(len(temp)):
            if temp[j][i] == '1':
                ones = ones + 1
            else:
                zeros = zeros + 1
        if ones < zeros:
            ideal = ideal + '1'
        else:
            ideal = ideal + '0'

        for j in range(len(data)):
            if (not data[j][i] == ideal[i]) and (data[j] in temp):
                temp.remove(data[j])
                if len(temp) == 1:
                    return temp[0]


print("problem 2:" + str(int(get_ox(inputs), 2) * int(get_co(inputs), 2)))
