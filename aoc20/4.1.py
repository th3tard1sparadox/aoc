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
        else:
            for item in l[:-1].split():
                field = item.split(':')
                cred.append(field[0])

    return valid


print(func())
print("time: " + str((time.time() - time1) * 1000) + "ms")
