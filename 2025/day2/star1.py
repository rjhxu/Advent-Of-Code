sm = 0

with open("2025/day2/input.txt") as f:
    line = f.read()
    line = line.split(",")
    for i in line:
        a, b = i.split("-")
        a = int(a)
        b = int(b)
        for i in range(a, b+1):
            n = str(i)
            if len(n)%2==0 and n[0:len(n)//2] == n[len(n)//2:]:
                sm+=i
print(sm)