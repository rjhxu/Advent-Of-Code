total = 0
for line in open("day2/input.txt", "r"):
    ar = list(map(int, line.split()))
    for i in range(len(ar)):
        safe = True
        nar = ar[:i] + ar[i+1:]
        if( nar == sorted(nar) or nar==sorted(nar, reverse=True)):
            for i in range(len(nar) - 1):
                if(abs(int(nar[i])-int(nar[i+1]))>3 or int(nar[i])==int(nar[i+1])):
                    safe = False
            if(safe):
                total+=1
                break
print(total)