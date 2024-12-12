lis = open("2024/day11/input.txt", "r").readline().strip().split(" ")

for j in range(25):
    old = lis.copy()
    for i, s in enumerate(old):
        if(s=="0"):
            lis[i]="1"
        elif(len(s)%2):
            lis[i]=str(int(s)*2024)
        else:
            lis[i]=old[i][:len(s)//2]
            lis.append(str(int(old[i][len(s)//2:])))
    
print(len(lis))
