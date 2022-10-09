import time
import re


time1 = time.time()
def match(strg):
    return bool(re.search(r'^[a-z0-9]*$', strg))


def match_num(strg):
    return bool(re.search(r'^[0-9]*$', strg))


def func():
    input_f = open('input_4.1.txt', 'r')
    input_d = input_f.readlines()
    input_d.append('\n')
    
    invalid = False
    valid = 0
    creds = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    cred = []
    for i, l in enumerate(input_d):
        if l == '\n':
            for c in creds:
                if c not in cred:
                    invalid = True
                    break
            if not invalid:
                valid += 1
            invalid = False
            cred = []
        elif not invalid:
            for item in l[:-1].split():
                field = item.split(':')
                cred.append(field[0])
                if field[0] == 'byr':
                    if int(field[1]) < 1920 or int(field[1]) > 2002:
                        invalid = True
                if field[0] == 'iyr':
                    if int(field[1]) < 2010 or int(field[1]) > 2020:
                        invalid = True
                if field[0] == 'eyr':
                    if int(field[1]) < 2020 or int(field[1]) > 2030:
                        invalid = True
                if field[0] == 'hgt':
                    unit = field[1][-2:]
                    if unit == "cm":
                        if int(field[1][:-2]) < 150 or int(field[1][:-2]) > 193:
                            invalid = True
                    elif unit == "in":
                        if int(field[1][:-2]) < 59 or int(field[1][:-2]) > 76:
                            invalid = True
                    else:
                        invalid = True
                if field[0] == 'hcl':
                    if field[1][0] != '#':
                        invalid = True
                    elif len(field[1][1:]) != 6 :
                        invalid = True
                    elif not match(field[1][1:]):
                        invalid = True
                if field[0] == 'ecl':
                    if not field[1] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
                        invalid = True
                if field[0] == 'pid':
                    if len(field[1]) != 9 or not match_num(field[1]):
                        invalid = True

    return valid


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
