

DIRS = [(di, dj) for di in [-1, 0, 1] for dj in [-1, 0, 1] if not (di==0 and dj==0)]

def access(i, j, grid):
    count = 0
    for di, dj in DIRS:
        ni, nj = i+di, j+dj
        if 0<=ni<len(grid) and 0<=nj<len(grid[0]):
            if grid[ni][nj]=='@':
                count += 1
    return count

with open("2025/day4/input.txt") as f:
    rolls = 0
    grid = list(map(str.strip, f.readlines()))
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]=='@':
                rolls += access(i, j, grid) <4

print(rolls)

