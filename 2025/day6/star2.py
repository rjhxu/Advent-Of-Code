from math import prod
ans = 0

nums = []

with open("2025/day6/input.txt") as f:
    for line in f:
        if line[0].isnumeric():
            nums.append(line.strip())
        else:
            operations=line.strip().split()

terms = [[] for _ in range(len(operations))]
op_num = 0
for i in range(len(nums[0])):
    cur = -1
    for j in range(len(nums)):
        if nums[j][i].isnumeric():
            cur = (cur*10 + int(nums[j][i])) if cur!=-1 else int(nums[j][i])
    if cur == -1:
        op_num+=1
    else:
        terms[op_num].append(cur)

for i in range(len(operations)):
    ans = ans + (sum(terms[i]) if operations[i]=='+' else prod(terms[i]))

print(ans)
    
