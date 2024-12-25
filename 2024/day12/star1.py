grid = [list(line.strip()) for line in open("2024/day12/input.txt", "r")]
visited = set()
fences = []
seen = set()
cnt = 0
dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
def search(x, y, sym):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != sym:
        fences.append((x, y))
    elif not (x,y) in visited:
        visited.add((x,y))
        seen.add((x,y))
        for i in dirs:
            search(x+i[0], y+i[1], sym)
            
        

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if not (i, j) in seen:
            search(i, j, grid[i][j])
            cnt = cnt+len(fences)*len(visited)
            visited = set()
            fences = []

print(cnt)


