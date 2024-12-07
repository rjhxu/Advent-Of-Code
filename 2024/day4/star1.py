grid = open("2024/day4/input.txt", "r").read().split()
total = 0
dir = ((1,1), (1,0), (1,-1), (0,1), (0,-1), (-1,1), (-1,0), (-1,-1))
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if(grid[i][j]=='X'):
            for x, y in dir:
                if(i+x*3>=0 and i+x*3<len(grid) and j+y*3>=0 and j+y*3<len(grid[0])):
                    total+=(grid[i+x][j+y]=='M' and grid[i+2*x][j+2*y]=='A' and grid[i+3*x][j+3*y]=='S')

print(total)