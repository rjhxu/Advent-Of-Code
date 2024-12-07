from functools import cmp_to_key


def comp(x,y):
    if x in d and y in d[x]:
        return 1
    else:
        return -1
    
d = {}
pages = []
total = 0
for line in open("2024/day5/input.txt","r"):

    if '|' in line:
        ar = line.split("|")
        if ar[1].strip() in d:
            d[ar[1].strip()].append(ar[0])
        else:
            d[ar[1].strip()]=[ar[0]]

    elif ',' in line:
        pages =[]
        safe = True
        ar = line.split(',')
        ar[-1]=ar[-1].strip()
        for currentpage in ar:
            for seenpage in pages:
                for unallowedpage in d[seenpage]:
                    if(unallowedpage == currentpage.strip()):
                        safe = False
            if currentpage in d: 
                pages.append(currentpage)

        if(not safe):
            ar = sorted(ar, key=cmp_to_key(comp))
            total+=int(ar[len(ar)//2])
print(total)