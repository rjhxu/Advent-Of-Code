from dataclasses import dataclass

@dataclass
class Robot:
    pos_x: int
    pos_y: int
    vel_x: int
    vel_y: int

robots = []
for line in open("2024/day14/input.txt", "r"):
    pos, vel = line.split()
    px, py = map(int, pos[2:].split(','))
    vx, vy = map(int, vel[2:].split(','))
    robots.append(Robot(px, py, vx, vy))

current_robots = [Robot(r.pos_x, r.pos_y, r.vel_x, r.vel_y) for r in robots]
for i in range(100):
    for robot in current_robots:
        robot.pos_x = (robot.pos_x + robot.vel_x) % 101
        robot.pos_y = (robot.pos_y + robot.vel_y) % 103

mid_x = 101 // 2
mid_y = 103 // 2
quadrants = [0, 0, 0, 0]
for robot in current_robots:
    if robot.pos_x == mid_x or robot.pos_y == mid_y:
        continue
    if robot.pos_x < mid_x:
        if robot.pos_y < mid_y:
            quadrants[0] += 1
        else:
            quadrants[2] += 1
    else:
        if robot.pos_y < mid_y:
            quadrants[1] += 1 
        else:
            quadrants[3] += 1

print(quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])

