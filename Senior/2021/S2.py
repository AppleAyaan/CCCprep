m = int(input())
n = int(input())

k = int(input())

rows = [0] * m
cols = [0] * n

for i in range(k):
    stroke = input().split(' ')
    direction = stroke[0]
    index = int(stroke[1]) - 1

    if direction == 'R':
        rows[index] += 1
    else:
        cols[index] += 1

count = 0
for i in range(m):
    for j in range(n):
        if (rows[i] + cols[j]) % 2 == 1:
            count += 1

print(count)
