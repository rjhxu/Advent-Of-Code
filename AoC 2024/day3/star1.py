import re
total = 0
for line in open("day3/input.txt", "r"):
    for i in re.findall(r'mul\(\d+,\d+\)', line):
        total+=int(i[4:].split(",")[0]) * int(i[4:-1].split(",")[1])

print(total) 
    
