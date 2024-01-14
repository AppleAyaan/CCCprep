x = int(input())

n = [int(y) for y in input().split(' ')]

n.sort()
print(n)
if x % 2 == 0:
    pos1 = (x//2)-1
    pos2 = x//2

    p1List = n[:pos1]
    p2List = n[pos2:]

    p1List.reverse()
    p1List.insert(0, n[pos1])

    for i in range(len(n)//2):
        print(p1List[i], end = ' ')
        print(p2List[i], end = ' ')
else:
    pos1 = ((x+1)//2) - 1
    pos2 = pos1 + 1

    p1List = n[:pos1]
    p2List = n[pos2:]

    p1List.reverse()
    p1List.insert(0, n[pos1])

    for i in range(x):
        print(p1List[i], end = ' ')
        print(p2List[i], end = ' ')