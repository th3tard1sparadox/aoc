with open("input10.txt") as file:
    lines = file.readlines()


def matching(op, cl):
    if op == '(' and cl == ')' or\
       op == '[' and cl == ']' or\
       op == '{' and cl == '}' or\
       op == '<' and cl == '>':
        return True
    return False


def find_wrong():
    closing = [')', ']', '}', '>']
    points_per_char = [3, 57, 1197, 25137]
    points = 0
    wrong_lines = []
    for i, line in enumerate(lines):
        stack = []
        for char in line:
            if char in closing:
                if not matching(stack.pop(), char):
                    wrong_lines.append(i)
                    points += points_per_char[closing.index(char)]
                    break
            else:
                stack.append(char)
    for i in wrong_lines:
        lines[i] = ''
    return points


print("part 1:" + str(find_wrong()))


def complete_lines():
    opening = ['(', '[', '{', '<']
    closing = [')', ']', '}', '>']
    scores = []
    for line in lines:
        line_score = 0
        if not line == '':
            stack = []
            for char in line:
                if char in opening:
                    stack.append(char)
                elif char in closing:
                    stack.pop()
            stack.reverse()
            for cl in stack:
                line_score *= 5
                line_score += opening.index(cl) + 1
            scores.append(line_score)
    scores.sort()
    return scores[len(scores) // 2]


print("part 2:" + str(complete_lines()))
