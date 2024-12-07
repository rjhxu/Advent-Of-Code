dirs= ((-1,0),(0,1), (1,0), (0,-1))
grid = [list(line.strip()) for line in open("2024/day6/input.txt", "r")]
direction = 0
total = 0
x, y = -1, -1
for i in range(len(grid)):
    if '^' in grid[i]:
        x= i
        y = grid[i].index('^')

while x>=0 and x<len(grid) and y>=0 and y<len(grid[0]):
    if(grid[x][y]=='#'):
        x-=dirs[direction%4][0]
        y-=dirs[direction%4][1]
        direction+=1
    else:
        grid[x][y]="X"
        x+=dirs[direction%4][0]
        y+=dirs[direction%4][1]

for i in range(len(grid)):
    total+=grid[i].count("X")
        
print(total)

    



