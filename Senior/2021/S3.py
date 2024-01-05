n = int(input())
pos = []
speed = []
hear = []

l = float('inf')
r = 0

for i in range(n):
    p, w, d = [int(x) for x in input().split(' ')]
    pos.append(p)
    speed.append(w)
    hear.append(d)
    if p > r:
        r = p
    if p < l:
        l = p 

def time(x):
    time = 0
    for i in range(n):
        walk = abs(x-pos[i]) - hear[i]
        if walk > 0:
            time += walk * speed[i]
    return time

while l <= r:
    mid = (l+r)//2
    score = time(mid)
    leftScore = time(mid-1)
    rightScore = time(mid+1)
    if score <= leftScore and score <= rightScore:
        break
    elif score < rightScore:
        r = mid-1
    elif score < leftScore:
        l = mid+1

print(score)