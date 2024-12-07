total = 0
for line in open("2024/day2/input.txt", "r"):
    ar = list(map(int, line.split()))
    safe = True
    if( ar == sorted(ar) or ar==sorted(ar, reverse=True)):
        for i in range(len(ar) - 1):
            if(abs(int(ar[i])-int(ar[i+1]))>3 or int(ar[i])==int(ar[i+1])):
                safe = False
        if(safe):
            total+=1
print(total)