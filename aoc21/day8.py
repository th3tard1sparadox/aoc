from itertools import permutations

def func():
    with open("input8.txt") as file:
        inputs = file.readlines()

    notes = [[j[:-1] for j in i.split('| ')] for i in inputs]

    perm = [''.join(p) for p in permutations('abcdefg')]

    def check_num(num):
        numbers = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']
        num = ''.join(sorted(num))
        return num in numbers


    def change_num(perm, num):
        reg = 'abcdefg'
        new_num = ''
        for i in num:
            new_num += reg[perm.find(i)]
        return new_num


    def iter_pos(numbers, looking_for):

        count = 0
        for note in numbers:
            for p in perm:
                ok_perm = True
                for t in note[0].split(' '):
                    if not check_num(change_num(p, t)):
                        ok_perm = False
                        break
                if not ok_perm:
                    continue
                for t in note[1].split(' '):
                    if ''.join(sorted(change_num(p, t))) in looking_for:
                        count += 1
                break

        return count


    print("part 1:" + str(iter_pos(notes, ['cf', 'bcdf', 'acf', 'abcdefg'])))


    def find_outputs(numbers):
        valid_numbers = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

        count = 0
        for note in numbers:
            for p in perm:
                ok_perm = True
                for t in note[0].split(' '):
                    if not check_num(change_num(p, t)):
                        ok_perm = False
                        break
                if not ok_perm:
                    continue
                num = ''
                for t in note[1].split(' '):
                    n = valid_numbers.index(''.join(sorted(change_num(p, t))))
                    num += str(n)
                count += int(num)
                break

        return count


    print("part 2:" + str(find_outputs(notes)))

func()
