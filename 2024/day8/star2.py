grid = [list(line.strip()) for line in open("2024/day8/input.txt", "r")]
dic = {}
antinodeset= set()
total = 0
#adding the coordinates of each alphanumeric value to dic
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if(grid[i][j]!='.'):

            if(not (grid[i][j] in dic)):

                dic[grid[i][j]]=set()

            dic[grid[i][j]].add((i, j))

#calculate antinodes
for i in dic:
    for x, y in dic[i]:
        for nx, ny in dic[i]:
            if (nx, ny) != (x, y):
                antinodeset.add((x,y))
                dx, dy = nx - x, ny - y
                
                pos1 = (x - dx, y - dy)
                pos2 = (nx + dx, ny + dy)
                while 0 <= pos1[0] < len(grid) and 0 <= pos1[1] < len(grid[0]):
                    antinodeset.add(pos1)
                    pos1 = (pos1[0] - dx, pos1[1] - dy) 

                while 0 <= pos2[0] < len(grid) and 0 <= pos2[1] < len(grid[0]):
                    antinodeset.add(pos2)
                    pos2 = (pos2[0] + dx, pos2[1] + dy)  

print(len(antinodeset))