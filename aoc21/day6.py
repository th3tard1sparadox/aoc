with open("input6.txt") as file:
    inputs = file.readlines()

fish = [int(i) for i in inputs[0].split(',')]
fish_stages = {}
for i in range(9):
    fish_stages[i] = fish.count(i)


def sim_fish(fish, days):
    for d in range(days):
        next_day = {}
        for i in range(9):
            if i == 6:
                next_day[i] = fish[i + 1] + fish[0]
            else:
                next_day[i] = fish[(i + 1) % 9]
        fish = next_day.copy()
    return sum(fish.values())


print("part 1:" + str(sim_fish(fish_stages, 80)))
print("part 2:" + str(sim_fish(fish_stages, 256)))
