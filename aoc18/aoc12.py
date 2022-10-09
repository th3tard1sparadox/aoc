with open("pattern.txt") as file:
    inputs = file.readlines()

BUFFER = 10
ITERATIONS = 50_000_000_000

state = '.' * BUFFER + "..##.#######...##.###...#..#.#.#..#.##.#.##....####..........#..#.######..####.#.#..###.##..##..#..#" + '.' * 102

gives_empty = {line[:5] for line in inputs if line[-2] == '.'}

pattern_iterations = 99
for i in range(pattern_iterations):
    next_gen = ""
    for i in range(2, len(state) - 2):
        if state[i-2:i+3] in gives_empty:
            next_gen += '.'
        else:
            next_gen += '#'

    next_gen = ".." + next_gen + ".."

    #print(next_gen[next_gen.index('#'):-next_gen[::-1].index('#')])
    state = next_gen


pots = state.count('#')

final_sum = 0
for i, pot in enumerate(state):
    if pot == '#':
        final_sum += i - BUFFER

final_sum += pots * (ITERATIONS - pattern_iterations)

print(final_sum)

