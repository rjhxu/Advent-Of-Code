cur = 50
cnt = 0
prev = None
with open ("2025/day1/input.txt") as f:
    for line in f:
        sign = 1 if line[0]=="R" else -1
        d = int(line[1:])
        remaining_steps = (100 - cur) if sign == 1 else cur
        if remaining_steps == 0:
            remaining_steps = 100
        if remaining_steps <=d:
            cnt+= 1+(d-remaining_steps)//100
        cur+=sign*d
        cur%=100


print(cnt)
