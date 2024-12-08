total= 0
for line in open("2024/day7/input.txt", "r"):
    test = int(line.split(":")[0])
    nums = line.split(":")[1].strip().split()
    for i in range(3**(len(nums)-1)):
        start = int(nums[0])
        ternary_rep = ""
        while i > 0:
            ternary_rep = str(i % 3) + ternary_rep
            i //= 3
        ternary_rep = ternary_rep.zfill(len(nums)-1)

        for j in range(1, len(nums)):
            if(ternary_rep[j-1]=='0'):
                start*=int(nums[j])
            elif(ternary_rep[j-1]=='1'):
                start+=int(nums[j])
            else:
                start = start*(10**len(nums[j])) + int(nums[j])
        if(start==test):
            total+=test
            break
print(total)