# partial marks awarded
# 7/15 - TLE error on BATCH 3 

x = int(input())
xList = []
for i in range(x):
    x1 = input().split(' ')
    xList.append(x1[0])
    xList.append(x1[1])

y = int(input())
yList = []
for j in range(y):
    y1 = input().split()
    yList.append(y1[0])
    yList.append(y1[1])


violations = 0


g = int(input())
gList = []
for k in range(g):
    gList.append(input().split(' '))

for a in range(0, len(xList), 2):
    for l in range(len(gList)):
        isThere = 0
        
        if xList[a] in gList[l]:
            isThere += 1
        if xList[a + 1] in gList[l]:
            isThere += 1
        if isThere == 1:
            violations += 1
            break

for b in range(0, len(yList), 2):
    for m in range(len(gList)):
        isntThere = 0

        if yList[b] in gList[m]:
            isntThere += 1
        if yList[b+1] in gList[m]:
            isntThere += 1
        if isntThere == 2:
            violations += 1

print(violations)