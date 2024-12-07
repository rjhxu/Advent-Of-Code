id1 = []
id2 = []
sum = 0
for line in open("2024/day1/input.txt", "r"):
    ltokens = line.split()
    id1.append(int(ltokens[0]))
    id2.append(int(ltokens[1]))

for a,b in zip(id1, id2):
    sum+=abs(a-b)

print(sum)