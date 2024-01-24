k = int(input())

total = []
num = 0

for i in range(k):
    x = int(input())

    if x == 0:
        total.pop()
    else:
        total.append(x)


for j in total:
    num += j

print(num)