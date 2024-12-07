# wrong answer
# import re
# total = 0
# on = True
# for line in open("day3/input.txt", "r"):
#     for i in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line):
#         if(on and i.startswith('mul') ):
#             total+=int(i[4:].split(",")[0]) * int(i[4:-1].split(",")[1])
#         elif(i.startswith('don')):
#             on = False
#         else:
#             on = True

# print(total) 


import re
total = 0
on = True
for line in open("2024/day3/input.txt", "r"):
    for i in re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", line):
        if(i.startswith('mul') ):
            total+=on*int(i[4:].split(",")[0]) * int(i[4:-1].split(",")[1])
        elif(i.startswith('don')):
            on = False
        else:
            on = True

print(total) 