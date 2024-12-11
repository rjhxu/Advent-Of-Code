dirs= ((-1,0),(0,1), (1,0), (0,-1))
grid = [list(map(int, line.strip())) for line in open("2024/day10/input.txt", "r")]
total = 0

def search(x, y, num):
    if not (0 <= x < len(grid) and 0 <= y < len(grid[0])) or grid[x][y] != num + 1:
        return 0
    if(grid[x][y]==9):
        return 1
    return sum(search(x+dx, y+dy, num+1) for dx, dy in dirs)
    
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if(not grid[i][j]):
            paths = search(i, j, -1)
            total+=paths
            print(paths)

print(total)