with open('Polymer.txt') as file:
    polymer = file.readlines()

def it_search(seq):
    removed = True

    while removed:
        removed = False
        for i, letter in enumerate(seq):
            if i >= len(seq) - 1:
                break
            elif letter.lower() == seq[i + 1].lower():
                if letter.isupper() and seq[i + 1].islower():
                    seq = seq[:i] + seq[i + 2:]
                    removed = True
                    break
                elif letter.islower() and seq[i + 1].isupper():
                    seq = seq[:i] + seq[i + 2:]
                    removed = True
                    break

    return seq

def rm_first(seq):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    lowest = 10**50
    
    for letter in alphabet:
        print(letter)
        new_seq = seq
        for i, part in enumerate(new_seq):
            if part.lower() == letter:
                new_seq = new_seq.replace(part, "")
        temp = len(it_search(new_seq))
        if temp < lowest:
            lowest = temp

    return lowest

print(rm_first(it_search(polymer[0])))
