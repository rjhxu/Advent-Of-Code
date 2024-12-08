total= 0
for line in open("2024/day7/input.txt", "r"):
    test = int(line.split(":")[0])
    nums = line.split(":")[1].strip().split()
    for i in range(2**(len(nums)-1)):
        start = int(nums[0])
        instructions = [j == '1' for j in bin(i)[2:].zfill(len(nums)-1)]
        for j in range(1, len(nums)):
            if(instructions[j-1]):
                start*=int(nums[j])
            else:
                start+=int(nums[j])
        if(start==test):
            total+=test
            break
print(total)

