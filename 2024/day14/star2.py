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
seconds= 0 

while True:
    seconds+=1
    for robot in current_robots:
        robot.pos_x = (robot.pos_x + robot.vel_x) % 101
        robot.pos_y = (robot.pos_y + robot.vel_y) % 103

    positions = {(robot.pos_x, robot.pos_y) for robot in current_robots}
    if len(positions) == len(current_robots):
        print(seconds)
        grid = [['.'] * 101 for _ in range(103)]
        for robot in current_robots:
            x, y = robot.pos_x, robot.pos_y
            if grid[y][x] == '.':
                grid[y][x] = '1'
            else:
                grid[y][x] = str(int(grid[y][x]) + 1)
        visualization = '\n'.join(''.join(row) for row in grid)
        print(visualization)
        break

        
