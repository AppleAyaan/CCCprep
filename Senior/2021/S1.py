n = int(input())

line = input().split(' ')
line2 = input().split(' ')

h = []
w = []

for i in range(n+1):
    h.append(int(line[i]))

for i in range(n):
    w.append(int(line2[i]))

total = 0

for i in range(n):
    total += (h[i] + h[i+1]) * w[i] / 2

print(total)