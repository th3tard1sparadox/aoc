with open("map.txt") as file:
    inputs = file.readlines()

cart_map = [[char for char in line] for line in inputs]

carts = []
for y, line in enumerate(cart_map):
    for x, char in enumerate(line):
        if char == '<' or char == '>':
            carts.append(((x, y), 0, char))
            cart_map[y][x] = '-'
            
        elif char == '^' or char == 'v':
            carts.append(((x, y), 0, char))
            cart_map[y][x] = '|'

for line in cart_map:
    print("".join(line))

def turn_right(cart):
    if cart[2] == '<':
        return(cart[0], cart[1], '^')
    elif cart[2] == '>':
        return(cart[0], cart[1], 'v')
    elif cart[2] == '^':
        return(cart[0], cart[1], '>')
    elif cart[2] == 'v':
        return(cart[0], cart[1], '<')

def turn_left(cart):
    if cart[2] == '<':
        return(cart[0], cart[1], 'v')
    elif cart[2] == '>':
        return(cart[0], cart[1], '^')
    elif cart[2] == '^':
        return(cart[0], cart[1], '<')
    elif cart[2] == 'v':
        return(cart[0], cart[1], '>')

def move(cart):
    if cart[2] == '<':
        return((cart[0][0] - 1, cart[0][1]), cart[1], cart[2])
    elif cart[2] == '>':
        return((cart[0][0] + 1, cart[0][1]), cart[1], cart[2])
    elif cart[2] == '^':
        return((cart[0][0], cart[0][1] - 1), cart[1], cart[2])
    elif cart[2] == 'v':
        return((cart[0][0], cart[0][1] + 1), cart[1], cart[2])

def update(cart):
    cart = move(cart)
    if cart_map[cart[0][1]][cart[0][0]] == '/':
        if cart[2] == '<' or cart[2]  == '>':
            cart = turn_left(cart)
        elif cart[2] == '^' or cart[2]  == 'v':
            cart = turn_right(cart)

    elif cart_map[cart[0][1]][cart[0][0]] == '\\':
        if cart[2] == '<' or cart[2]  == '>':
            cart = turn_right(cart)
        elif cart[2] == '^' or cart[2]  == 'v':
            cart = turn_left(cart)

    elif cart_map[cart[0][1]][cart[0][0]] == '+':
        if cart[1]%3 == 0:
            cart = turn_left(cart)
        elif cart[1]%3 == 2:
            cart = turn_right(cart)
        cart = (cart[0], cart[1] + 1, cart[2])

    return cart    

while len(carts) > 1:
    for i, cart in enumerate(carts):
        if not cart == 'X':
            carts[i] = update(cart)
            for check in carts:
                if carts[i][0] == check[0] and i != carts.index(check):
                    carts[i] = 'X'
                    carts[carts.index(check)] = 'X'
               
    for i in range(carts.count('X')):
        carts.remove('X')
            
    carts.sort(key=lambda pos: pos[0])
print(carts)
