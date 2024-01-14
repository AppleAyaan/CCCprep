x = int(input())
list = []

for i in range(x):
    list.append(int(input()))

list.sort()
x3 = []


for i in range(1, len(list)-1):
    x1 = (list[i] - list[i-1]) / 2
    x2 = (list[i] - list[i+1]) / 2
    x1 = abs(x1)
    x2 = abs(x2)
    x3.append(x1 + x2)


min = min(x3)
print("%.1f" %min)