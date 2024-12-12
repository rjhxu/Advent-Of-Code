lis = list(map(int, open("2024/day11/input.txt", "r").readline().strip().split(" ")))
dic = {}

def check(n, blink):
    if not blink:
        return 1
    if((n, blink) not in dic):
        if not n:
            dic[(n, blink)] = check(1, blink-1)
        elif len(str(n))%2:
            dic[(n, blink)] = check(n*2024, blink -1)
        else:
            dic[(n,blink)] = check(int(str(n)[:len(str(n))//2]), blink-1) + check(int(str(n)[len(str(n))//2:]), blink-1)
        
    return dic[(n,blink)]

print(sum(check(i, 75) for i in lis))