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
        lowest_dist = 1000
        lowest_point = ()
        for point in inputs:
            found_same = False
            dist = manhattan_dist(point, (x, y))
            if dist == lowest_dist:
                found_same = True
            if dist < lowest_dist:
                lowest_dist = manhattan_dist(point, (x, y))
                lowest_point = point

        if not found_same:
            lowest_dic[(x, y)] = lowest_point
        else:
            lowest_dic[(x, y)] = '.'

infinate = set()
for x in range(lowestx - 1, highestx + 2):
    infinate.add(lowest_dic[(x, lowesty - 1)])
    infinate.add(lowest_dic[(x, highesty + 1)])

for y in range(lowesty, highesty + 1):
    infinate.add(lowest_dic[(lowestx - 1, y)])
    infinate.add(lowest_dic[(highestx + 1, y)])

largest = 0
for point in inputs:
    if not point in infinate:
        size = sum(compare == point for compare in lowest_dic.values())
        if size > largest:
            largest = size

print(largest)
        
