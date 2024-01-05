#TLE ERROR on batch 3
#Olog(n)^2 complexity 

n = int(input())

pos = []
speed = []
posDupe = []
total = [0]

for i in range(n):
    p, t = [int(x) for x in input().split()]
    pos.append(p)
    speed.append(t)

for j in range(len(pos)):
    posDupe.append(pos[j])
posDupe.sort()

for i in range(1, len(speed)):
    x = posDupe[i] - posDupe[i-1]

    a = posDupe[i-1]
    b = posDupe[i]

    c = pos.index(a)
    d = pos.index(b)

    y = speed[d] - speed[c]

    if abs(y/x) > total[0]:
        total.append(abs(y/x))
    
print(max(total))