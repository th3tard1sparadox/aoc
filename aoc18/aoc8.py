with open("tree.txt") as file:
    inputs = file.readlines()[0].split()

inputs = [int(i) for i in inputs]

def tree_length(tree):
    if not tree:
        return 0
    if tree[0] == 0:
        return tree[1] + 2
    else:
        length = 0
        for i in range(tree[0]):
            length += tree_length(tree[2 + length:])
        return tree[1] + 2 + length

def sum_tree(tree):
    if not tree:
        return 0
    else:
        temp_sum = 0
        current_length = 0
        previous_length = 0
        under_trees = []
        for i in range(tree[0]):
            if i < 1:
                current_offset = 2 + previous_length
            else:
                current_offset = previous_length
            current_length = tree_length(tree[current_offset:])
            under_trees.append(sum_tree(tree[current_offset:current_length + current_offset]))
            previous_length = current_offset + current_length
        if tree[0] == 0:
            current_sum = sum(tree[-tree[1]:])
        else:
            current_sum = 0
            for i in range(1, tree[1] + 1):
                if tree[-i] <= len(under_trees):
                    current_sum += under_trees[tree[-i] - 1]
        return temp_sum + current_sum

#138
#print(sum_tree([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]))
print(sum_tree(inputs))
#47
#print(sum_tree([3, 2, 2, 2, 1, 1, 0, 1, 2, 3, 0, 2, 4, 2, 7, 1, 2, 1, 1, 1, 0, 1, 3, 1, 2, 1, 0, 1, 7, 1, 1, 0, 1, 1, 2, 1, 1, 0, 2, 5, 2, 3, 2])) #10
#print(sum_tree([1, 2, 2, 2, 1, 1, 0, 1, 2, 3, 0, 2, 4, 2, 7, 1, 3, 2]))
#print(sum_tree([2, 2, 1, 2, 2, 2, 0, 1, 1, 0, 1, 1, 1, 1, 2, 1, 0, 1, 1, 1, 1]))
#21
#print(sum_tree([4, 2, 0, 1, 3, 0, 1, 4, 0, 1, 5, 0, 1, 6, 1, 2]))
