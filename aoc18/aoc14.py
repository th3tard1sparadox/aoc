recipe_list = [3, 7]
elf1 = 0
elf2 = 1
not_found = True

while not_found:
    new_score = recipe_list[elf1] + recipe_list[elf2]

    for i in range(len(str(new_score))):
        recipe_list.append(int(str(new_score)[i]))
        if len(recipe_list) > 6 and recipe_list[-6:] == [8, 2, 4, 5, 0, 1]:
            print(len(recipe_list [:-6]))
            not_found = False

    elf1 += recipe_list[elf1] + 1
    elf1 = elf1 % len(recipe_list)
    elf2 += recipe_list[elf2] + 1
    elf2 = elf2 % len(recipe_list)

