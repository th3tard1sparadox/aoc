def split_input(seq):
    return [ID for ID in seq.split()]

def boxes(seq):
    IDs = split_input(seq)
    threes = 0
    twos = 0
    for ID in IDs:
        found_three = False
        found_two = False
        for letter in ID:
            if ID.count(letter) == 2 and found_two == False:
                twos += 1
                found_two = True
            elif ID.count(letter) == 3 and found_three == False:
                threes += 1
                found_three = True
    print(twos * threes)

def find_fabric(seq):
    IDs = split_input(seq)
    for i in range(len(IDs) - 1):
        for j in range(1, len(IDs) - i - 1):
            fault = 0
            if IDs[i] == IDs[i + j]:
                break
            for k in range(len(IDs[i])):
                if IDs[i][k] != IDs[i + j][k]:
                    if fault == 0:
                        fault += 1
                    else:
                        fault += 1
                        break
            if fault == 1:
                print(IDs[i], IDs[i + j])
