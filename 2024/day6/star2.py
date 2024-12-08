dirs= ((-1,0),(0,1), (1,0), (0,-1))
grid = [list(line.strip()) for line in open("2024/day6/input.txt", "r")]
total = 0
tx, ty = 92,74
for i in range(len(grid)):
    if '^' in grid[i]:
        tx= i
        ty = grid[i].index('^')

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j]=='.':
            visited = set()
            direction = 0
            grid[i][j]='#'
            x, y = tx, ty
            
            while 0<= x<len(grid) and 0<= y<len(grid[0]):
                if(grid[x][y]=='#'):
                    x-=dirs[direction%4][0]
                    y-=dirs[direction%4][1]
                    direction+=1
                else:
                    x+=dirs[direction%4][0]
                    y+=dirs[direction%4][1]
                if (x, y, direction%4) in visited:
                    total+=1
                    break
                visited.add((x, y, direction%4))
            
            grid[i][j]='.'
        
print(total)