grid = open("2024/day4/input.txt", "r").read().split()
total = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if(grid[i][j]=='M'):
            if(i+2<len(grid) and j+2<len(grid[0])):
                total+=(grid[i+1][j+1]=='A' and grid[i+2][j+2]=='S' and ((grid[i][j+2]=='M' and grid[i+2][j]=='S') or (grid[i][j+2]=='S' and grid[i+2][j]=='M')))
        elif(grid[i][j]=='S'):
            if(i+2<len(grid) and j+2<len(grid[0])):
                total+=(grid[i+1][j+1]=='A' and grid[i+2][j+2]=='M' and ((grid[i][j+2]=='M' and grid[i+2][j]=='S') or (grid[i][j+2]=='S' and grid[i+2][j]=='M')))

print(total)