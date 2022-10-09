with open("goblin_map.txt") as file:
    inputs = file.readlines()

cavern = set()
for y, line in enumerate(inputs):
    for x, char in enumerate(line):
        if char == "#":
            cavern.add((x, y))
dies = True
ad = 3
while dies:
    died = False
    ad += 1
    units = {}
    for y, line in enumerate(inputs):
        for x, char in enumerate(line):
            if char == "E":
                units[(x, y)] = (char, 200, ad)
            elif char == "G":
                units[(x, y)] = (char, 200, 3)

    def adjecent_keys(key):
        return [(key[0], key[1] - 1), (key[0] - 1, key[1]), (key[0] + 1, key[1]), (key[0], key[1] + 1)]

    def find_path(start_pos, goals):
        path_dic = {}
        queue = []
        queue.append(start_pos)
        visited = set()
        while queue:
            current = queue.pop()
            visited.add(current)

            if current in goals:
                while path_dic[current] != start_pos:
                    current = path_dic[current]
                return current

            for key in adjecent_keys(current):
                if key not in visited and key not in cavern and key not in list(units.keys()) and key not in queue:
                    path_dic[key] = current
                    queue.insert(0, key)

        return []

    def attack(pos, enemies, elf):
        global died
        lowest_hp = 200
        for key in adjecent_keys(pos):
            if key in enemies and units[key][1] < lowest_hp:
                lowest_hp = units[key][1]

        if elf:
            attackp = ad
        elif not elf:
            attackp = 3

        for key in adjecent_keys(pos):
            if key in enemies and units[key][1] == lowest_hp:
                units[key] = (units[key][0], units[key][1] - attackp, units[key][2])
                if units[key][1] <= 0:
                    del units[key]
                    if elf != True:
                        died = True
                    return key
                break
        return None

    rounds = 0
    can_move = True
    while can_move:
        sorted_positions = sorted(units.keys(), key=lambda pos: (pos[1], pos[0]))
        removed_keys = []
        for key in sorted_positions:
            if key not in removed_keys:
                if units[key][0] == "E":
                    enemy_sort = "G"
                    is_elf = True
                
                elif units[key][0] == "G":
                    enemy_sort = "E"
                    is_elf = False

                targets = []
                for pos, unit in units.items():
                    if unit[0] == enemy_sort:
                        targets.append(pos)

                targets = sorted(targets, key=lambda pos: (pos[1], pos[0]))

                in_range = []
                for target in targets:
                    for pos in adjecent_keys(target):
                        if pos not in cavern and pos not in units.keys():
                            in_range.append(pos)

                path = find_path(key, in_range)
                moved = False

                on_goal = False
                for pos in adjecent_keys(key):
                    if pos in targets:
                        on_goal = True

                if path != [] and not on_goal:
                    units[path] = units[key]
                    del units[key]
                    moved = True

                if moved == True:
                    removed_keys.append(attack(path, targets, is_elf))

                else:
                    removed_keys.append(attack(key, targets, is_elf))

                for unit in units.values():
                    if not unit[0] == list(units.values())[0][0]:
                        can_move = True
                        break
                    else:
                        can_move = False
                        
        rounds += 1
        removed_keys = []

    hp_sum = sum([unit[1] for unit in units.values()])

    if not died:
        print((rounds - 1) * hp_sum)
        break
