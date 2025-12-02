sm = 0

with open("2025/day2/input.txt") as f:
    line = f.read()
    line = line.split(",")
    for id_range in line:
        first_id, second_id = id_range.split("-")
        for id in range(int(first_id), int(second_id)+1):
            n = str(id)
            if len(n)%2==0 and n[0:len(n)//2] == n[len(n)//2:]:
                sm+=id
print(sm)