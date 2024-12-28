grid = [list(line.strip()) for line in open("2024/day12/input.txt", "r")]
visited, seen = set(), set()
dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
cnt = 0

def search(x, y, sym):
    if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] == sym and (x, y) not in visited:
        visited.add((x, y))
        seen.add((x, y))
        for dx, dy in dirs:
            search(x + dx, y + dy, sym)

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) not in seen:
            search(i, j, grid[i][j])
            corners = sum(
                ((x - 1, y) not in visited and (x, y - 1) not in visited) +
                ((x + 1, y) not in visited and (x, y - 1) not in visited) +
                ((x - 1, y) not in visited and (x, y + 1) not in visited) +
                ((x + 1, y) not in visited and (x, y + 1) not in visited) +
                ((x - 1, y) in visited and (x, y - 1) in visited and (x - 1, y - 1) not in visited) +
                ((x + 1, y) in visited and (x, y - 1) in visited and (x + 1, y - 1) not in visited) +
                ((x - 1, y) in visited and (x, y + 1) in visited and (x - 1, y + 1) not in visited) +
                ((x + 1, y) in visited and (x, y + 1) in visited and (x + 1, y + 1) not in visited)
                for x, y in visited
            )
            cnt += corners * len(visited)
            # print(f"A region of {grid[i][j]} with price of {len(visited)} * {corners} = {corners * len(visited)}")
            visited.clear()

print(cnt)
