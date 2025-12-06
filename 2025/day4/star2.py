DIRS = [(di, dj) for di in [-1, 0, 1] for dj in [-1, 0, 1] if not (di==0 and dj==0)]

def remove(H, W, access, stack):
    rolls = 0
    while stack:
        i, j = stack.pop()
        if access[i][j]==-1:
            continue
        access[i][j]=-1
        rolls+=1
        for di, dj in DIRS:
            ni, nj = i+di, j+dj
            if 0<=ni<H and 0<=nj<W and access[ni][nj]!=-1:
                access[ni][nj]-=1
                if access[ni][nj]<4:
                    stack.append((ni, nj))
    return rolls

with open("2025/day4/input.txt") as f:
    grid = [list(row.strip())for row in f.readlines()]
    H = len(grid)
    W = len(grid[0])
    access = [[0]*W for _ in range(H)]
    for i in range(H):
        for j in range(W):
            access[i][j] = -1 if grid[i][j]=='.' else 0
    for i in range(H):
        for j in range(W):
            if grid[i][j]=='@':
                for di, dj in DIRS:
                    ni, ji = i+di, j+dj
                    if 0<=ni<H and 0<=ji<W and grid[ni][ji]=='@':
                        access[ni][ji] += 1
stack = []
for i in range(H):
    for j in range(W):
        if -1<access[i][j]<4:
            stack.append((i, j))

print(remove(H, W, access, stack))

