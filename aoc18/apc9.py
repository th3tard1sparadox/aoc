import math

linked_list = {}


def insert_val(linked_list, val1, val2, val3):
    linked_list[val1] = [val2, val3]
    linked_list[val2][1] = val1
    linked_list[val3][0] = val1

    return linked_list


def remove_val(linked_list, val):
    left = linked_list[val][0]
    right = linked_list[val][1]
    linked_list[left][1] = right
    linked_list[right][0] = left

    del linked_list[val]

    return linked_list


def traverse_list(linked_list, steps, start):
    current = start

    if steps < 0:
        j = 0
    else:
        j = 1
        
    for i in range(abs(steps)):
        current = linked_list[current][j]

    return current


player_scores = {}
for i in range(416):
    player_scores[i] = 0

played = insert_val(linked_list, 0, 0, 0)
current = 0

current_player = 0
for i in range(1, (71975 * 100) + 1):
    j = current_player % len(player_scores)
    if i % 23 == 0:
        player_scores[j] += i
        temp = current
        current = traverse_list(played, -6, temp)
        remove = traverse_list(played, -7, temp)
        player_scores[j] += remove
        played = remove_val(played, remove)
    else:
        played = insert_val(played, i, traverse_list(played, 1, current), traverse_list(played, 2, current))
        current = i
    current_player += 1

winner = max(player_scores.values())
print(winner)
