grid = [list(line.strip()) for line in open("2024/day8/input.txt", "r")]
dic = {}
antinodeset= set()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if(grid[i][j]!='.'):

            if(not (grid[i][j] in dic)):

                dic[grid[i][j]]=set()

            dic[grid[i][j]].add((i, j))

for i in dic:
    for x, y in dic[i]:
        for nx, ny in dic[i]:
            if (nx, ny) != (x, y):
                dx, dy = nx - x, ny - y
                
                if 0 <= x - dx < len(grid) and 0 <= y - dy < len(grid[0]):
                    antinodeset.add((x - dx, y - dy))
                if 0 <= nx + dx < len(grid) and 0 <= ny + dy < len(grid[0]):
                    antinodeset.add((nx + dx, ny + dy))


print(len(antinodeset))