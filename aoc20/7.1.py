import time


time1 = time.time()
def func():
    input_f = open('input_7.1.txt', 'r')
    input_d = input_f.readlines()

    rules = {}
    for rule in input_d:
        parts = rule.split('contain')
        con = []
        for i in parts[1].split(','):
            if i != " no other bags.\n":
                if i[len(i) - 1] == '\n':
                    if i[-3:-2] == 's':
                        con.append(i[3:-3])
                    else:
                        con.append(i[3:-2])
                elif i[len(i) - 1] == 's':
                    con.append(i[3:-1])
                else:
                    con.append(i[3:])
        rules[parts[0][:-2]] = con

    def rec(dic, key):
        for i in dic[key]:
            if i == "shiny gold bag":
                return True
            if rec(dic, i):
                return True
        return False

    count = 0
    for rule in rules:
        if rec(rules, rule):
            count += 1
    return count


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
