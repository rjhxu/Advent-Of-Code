line = open("2024/day9/input.txt", "r").readline().strip()
max_num = len(line)//2 + 1
str = []
checksum = 0
for i in range(len(line)):
    if(i%2):
        for i in range(int(line[i])):
            str.append(False)
    else:
        for i in range(int(line[i])):
            str.append(True)

dic = {} # store how many of each number there is
for i in range(max_num): #populate dictionary
    dic[i]=int(line[i*2])

while dic:
    for i in range(len(str)):
        if not dic:
            break

        elif str[i]:
            first_key = list(dic.keys())[0]
            checksum += i * first_key
            print(i,' * ', first_key)
            dic[first_key] -= 1
            
            if dic[first_key] == 0:
                dic.pop(first_key)
        else:
            last_key = list(dic.keys())[-1]
            checksum += i * last_key
            print(i,' * ', last_key)
            dic[last_key] -= 1
            
            if dic[last_key] == 0:
                dic.pop(last_key)
print(checksum)
