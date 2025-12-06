ranges = []
cnt = 0
with open("2025/day5/input.txt") as f:
    for line in f:
        if "-" in line:
            a, b = map(int, line.strip().split("-"))

            if len(ranges)!=0:
                found = False
                for i in range(len(ranges)):
                    c, d = ranges[i]
                    if a<c and c<b<d:
                        ranges[i]=(a, d)
                        found = True
                    elif a<c and b>d:
                        ranges[i] = (a, b)
                        found = True
                    elif b>d and c<a<d:
                        ranges[i] = (c, b)
                        found = True
                if found:
                    continue
            ranges.append((a, b))

        elif line.strip():
            id = int(line.strip())
            for a, b in ranges:
                if a<=id<=b:
                    cnt+=1
                    break
print(cnt)