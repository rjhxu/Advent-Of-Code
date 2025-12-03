total_joltage_output = 0
with open("2025/day3/input.txt") as file:
    for line in file:
        v = list(map(int, list(line.strip())))
        largest_num = max(v[:-1])
        total_joltage_output+=(10*largest_num) + max(v[v.index(largest_num)+1:])

print(total_joltage_output)
