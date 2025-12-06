ranges = []
cnt = 0

with open("2025/day5/input.txt") as f:
    for line in f:
        if "-" in line:
            a, b = map(int, line.strip().split("-"))
            ranges.append((a, b))

ranges.sort(key=lambda x: x[0])
ranges.reverse()
new_list = []

while ranges:
    x1, x2 = ranges.pop()
    while ranges and x2 >= ranges[-1][0]:
        y1, y2 = ranges.pop()
        x2 = max(x2, y2)
    new_list.append((x1, x2))

for a, b in new_list:
    cnt+=b-a+1
print(cnt)