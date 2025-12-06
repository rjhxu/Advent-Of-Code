ans = 0

with open("2025/day6/input.txt") as f:
    lines = [line.strip().split() for line in f]

psa = [0]*len(lines[0])
ppa = [1]*len(lines[0])
for line in lines:
    if line[0].isnumeric():
        line = list(map(int, line))
        for i in range(len(line)):
            psa[i]+=line[i]
            ppa[i]*=line[i]
    else:
        for i in range(len(line)):
            ans+=ppa[i] if line[i]=='*' else psa[i]

print(ans)
    