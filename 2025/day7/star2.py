with open("2025/day7/input.txt") as f:
    lines = [list(line.strip()) for line in f]

for line in lines:
    print(line)
beams = [0] * len(lines[0])

beams[lines[0].index("S")] = 1

for line in lines:
    for i in range(len(line)):
        if line[i]=='^' and beams[i]:
            paths = beams[i]
            beams[i]=0
            beams[i-1]+=paths
            beams[i+1]+=paths
        

print(sum(beams))