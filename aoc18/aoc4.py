from datetime import datetime

with open('guards.txt') as file:
    guard_list = file.readlines()

times = [line[1:17] for line in guard_list]

guard_actions = [line[19:-1] for line in guard_list]

dates = [datetime.strptime(ts, "%Y-%m-%d %H:%M") for ts in times]

combined_list = [(dates[i], guard_actions[i]) for i in range(len(dates))]
combined_list.sort()

times_on_duty = {}

fell_asleep = 0
woke_up = 0
asleep_list = []

for action in combined_list:
    if action[1][6] == '#':
        key = action[1].split()[1]
        if key not in times_on_duty:
            times_on_duty[key] = 0

    if action[1][0] == 'f':
        fell_asleep = action[0].minute

    if action[1][0] == 'w':
        woke_up = action[0].minute
        asleep_list.append((key, fell_asleep, woke_up))

asleep_dict = {}

for i in range(60):
    for rng in asleep_list:
        if i >= rng[1] and i < rng[2]:
            if (i, rng[0]) not in asleep_dict:
                asleep_dict[(i, rng[0])] = 1
            else:
                asleep_dict[(i, rng[0])] += 1
            

print(sorted(asleep_dict.items(), key=lambda x: x[1], reverse=True))


