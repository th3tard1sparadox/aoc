def ad(seq):
    inputs = [int(num[1:]) if num[0] == '+' else -int(num[1:]) for num in seq.split()]
    curr = 0
    comp = set()
    found = False
    while not found:
        curr, comp, found = ad2(inputs, curr, comp, found)
    print(curr)

def ad2(inputs, curr, comp, found):
    for num in inputs:
        curr += num
        if curr in comp:
            found = True
            return curr, comp, found
        comp.add(curr)
    return curr, comp, found
