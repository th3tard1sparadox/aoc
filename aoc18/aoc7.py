import string

with open("sleigh.txt") as file:
    inputs = file.readlines()

alphabet = list(string.ascii_uppercase)
dependencies = [(line[5:6], line[36:37]) for line in inputs]

dep_dic = {}
for letter in alphabet:
    dep_dic[letter] = ""

for dep in dependencies:
    dep_dic[dep[1]] += dep[0]

finished_tasks = []
while len(finished_tasks) < len(alphabet):
    for task, dep in dep_dic.items():
        if dep == "":
            finished_tasks.append(task)
            del dep_dic[task]
            for task1, dep1 in dep_dic.items():
                if task in dep1:
                    dep_dic[task1] = dep1.replace(task, "")
            break
    print(dep_dic)
    print(finished_tasks)

elfes = []
elf1 = [0]
elfes.append(elf1)
elf2 = [0]
elfes.append(elf2)
elf3 = [0]
elfes.append(elf3)
elf4 = [0]
elfes.append(elf4)
elf5 = [0]
elfes.append(elf5)

dep_dic = {}
for letter in alphabet:
    dep_dic[letter] = ""

for dep in dependencies:
    dep_dic[dep[1]] += dep[0]

finished_tasks = []
sec = 0
while len(finished_tasks) < len(alphabet):
    for i, elf in enumerate(elfes):
        if not elf[0]:
            if len(elf) > 1 and not elf[-1] in finished_tasks:
                finished_tasks.append(elf[-1])
                for task1, dep1 in dep_dic.items():
                    if elf[-1] in dep1:
                        dep_dic[task1] = dep1.replace(elf[-1], "")
            print("real:", elfes[i])
            for task, dep in dep_dic.items():
                print(dep)
                if dep == "":
                    print("real2:", elfes[i])
                    elfes[i].append(task)
                    del dep_dic[task]
                    elfes[i][0] = alphabet.index(task) + 1 + 60
                    break
        if elf[0] > 0:
            elf[0] -= 1
    sec += 1
    print(dep_dic)
    print("finished:", finished_tasks)
    print(elfes)
    print(sec)
