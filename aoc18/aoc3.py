def split_input(seq):
    values = seq.split()
    pos = []
    size = []
    IDs = []
    for val in values:
        if val[-1] == ':':
            pos.append(val)
        if 'x' in val:
            size.append(val)
        if val[0] == '#':
            IDs.append(val)

    squares = []

    for i in range(len(pos)):
        x = pos[i].split(',')
        x[0] = int(x[0])
        x[1] = int(x[1][:-1])
        x_val = (x[0], x[1])
        
        y = size[i].split('x')
        y[0] = int(y[0]) + x[0]
        y[1] = int(y[1]) + x[1]
        y_val = (y[0], y[1])

        id_num = IDs[i]
        
        squares.append([x_val, y_val, id_num])

    return squares

def find_size(seq):
    x_max = 0
    y_max = 0
    for val in seq:
        if val[1][0] > x_max:
            x_max = val[1][0]
        if val[1][1] > y_max:
            y_max = val[1][1]
    return (x_max, y_max)

def fabric_cut(seq):
    val_list = split_input(seq)
    fabric_size = find_size(val_list)

    print(val_list)

    fabric = [[0] * fabric_size[1] for i in range(fabric_size[0])]

    for val in val_list:
        for i in range(val[0][1], val[1][1]):
            for j in range(val[0][0], val[1][0]):
                fabric[j][i] += 1

    TheOne = True

    for val in val_list:
        for i in range(val[0][1], val[1][1]):
            for j in range(val[0][0], val[1][0]):
                if fabric[j][i] != 1:
                    TheOne = False
                    break
        if TheOne == True:
            print(val[2])

        TheOne = True
