with open("input1.txt") as file:
    inputs = file.readlines()

def find_req(mass):
    _mass = int(mass / 3) - 2
    return _mass

def first():
    _sum = 0
    for mass in inputs:
        _sum = _sum + find_req(int(mass))
    print(_sum)

def second():
    _sum = 0
    temp = 0;
    for mass in inputs:
        temp = find_req(int(mass))
        _sum = _sum + temp
        while find_req(temp) > 0:
            temp = find_req(temp)
            _sum = _sum + temp
    print(_sum)

first()
second()
