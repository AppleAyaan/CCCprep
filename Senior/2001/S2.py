#incomplete
n = int(input())
m = int(input())

numList = []

for i in range(n, m):
    numList.append(i)


j = 1

while (j*j) < len(numList):
    j += 1

#use j - 1 for width of columns
print(j-1)

