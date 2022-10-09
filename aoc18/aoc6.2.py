import math

with open("coordinates.txt") as file:
    inputs = file.readlines()

inputs = [(int(line.split(',')[0]), int(line.split(',')[1])) for line in inputs]
 
def manhattan_dist(point1, point2):
    dist = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    return dist


highestx = 0
lowestx = 10**10
highesty = 0
lowesty = 10**10
for point in inputs:
    if point[0] < lowestx:
        lowestx = point[0]
    elif point[0] > highestx:
        highestx = point[0]
    if point[1] < lowesty:
        lowesty = point[1]
    elif point[1] > highesty:
        highesty = point[1]

lowest_dic = {}
for x in range(lowestx - 1, highestx + 2):
    for y in range(lowesty - 1, highesty + 2):
        tot_dist = 0
        for point in inputs:
            dist = manhattan_dist(point, (x, y))
            tot_dist += dist

        if tot_dist < 10000:
            lowest_dic[(x, y)] = '#'
        else:
            lowest_dic[(x, y)] = '.'


size = sum(compare == '#' for compare in lowest_dic.values())

print(size)
        
