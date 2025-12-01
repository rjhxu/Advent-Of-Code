cur = 50
cnt = 0
with open ("2025/day1/input.txt") as f:
    for line in f:
        sign = 1 if line[0]=="R" else -1
        cur+= int(line[1:])*sign
        cur%=100
        cnt+= cur == 0
print(cnt)
