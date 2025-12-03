total_joltage_output = 0
with open("2025/day3/input.txt") as file:
    for line in file:
        v = list(map(int, list(line.strip())))
        largest_num = max(v[:-11])
        joltage = (10**11)*largest_num

        for i in range(10, -1, -1):
            idx = v.index(largest_num)
            v = v[idx+1:]
            largest_num = max(v[:-i if i>0 else None])
            joltage+=(10**i)*largest_num
        total_joltage_output+=joltage

print(total_joltage_output)
