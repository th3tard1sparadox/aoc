with open("stars.txt") as file:
    inputs = file.readlines()

stars = [(int(line[10:16]), int(line[17:24])) for line in inputs]
stars_vel = [(int(line[36:38]), int(line[39:42])) for line in inputs]

class Star:
    def __init__(self, x, y, x_vel, y_vel):
        self.x = x
        self.y = y
        self.x_vel = x_vel
        self.y_vel = y_vel

    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel

star_obj = [Star(stars[i][0], stars[i][1], stars_vel[i][0], stars_vel[i][1]) for i, star in enumerate(stars)]

height = 0
highesty = -(50**100)
lowesty = 50**100
counter = 0
while height != 9:
    highesty = -(50**100)
    lowesty = 50**100
    for star in star_obj:
        star.move()
        if star.y > highesty:
            highesty = star.y
        elif star.y < lowesty:
            lowesty = star.y
    height = highesty - lowesty
    counter += 1

highestx = -(50**100)
lowestx = 50**100
for star in star_obj:
    if star.x > highestx:
        highestx = star.x
    elif star.x < lowestx:
        lowestx = star.x

width = highestx - lowestx

for star in star_obj:
    star.x -= lowestx
    star.y -= lowesty

message = [[" " for j in range(width + 1)] for i in range(height + 1)]

for star in star_obj:
    message[star.y][star.x] = "#"

for line in message:
    print("".join(line))

print(counter)
