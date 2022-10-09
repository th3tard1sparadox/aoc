with open("input7.txt") as file:
    crabs = [int(i) for i in file.readline().split(',')]

crabs_pos = {}
for i in range(max(crabs) + 1):
    crabs_pos[i] = crabs.count(i)

def mov_cost(crabs_pos, pos):
    cost = 0
    for crab_pos, crabs in crabs_pos.items():
        cost += abs(crab_pos - pos) * crabs
    return cost


def iter_hpos(crabs, crabs_pos, cost_cal):
    min_cost = 9999999999999999999999999999999999
    for i in range(max(crabs)):
        cost = cost_cal(crabs_pos, i)
        if cost < min_cost:
            min_cost = cost
        else:
            break
    return min_cost


print("part 1:" + str(iter_hpos(crabs, crabs_pos, mov_cost)))


def mov_cost_exp(crabs_pos, pos):
    cost = 0
    for crab_pos, crabs in crabs_pos.items():
        n = abs(crab_pos - pos)
        cost += 1/2 * n * (n + 1) * crabs
    return cost


print("part 2:" + str(int(iter_hpos(crabs, crabs_pos, mov_cost_exp))))
