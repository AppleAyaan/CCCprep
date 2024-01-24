x = int(input())

n = int(input())

dmoj = input().split(' ')
peg = input().split(' ')

for k in range(n):
    dmoj[k] = int(dmoj[k])
    peg[k] = int(peg[k])

bikeList = []
bikeSpeed = []
total = 0

dmoj.sort()
peg.sort()


if x == 1:
    for i in range(n):
        bikeList.append(dmoj[i])
        bikeList.append(peg[i])

        
    for j in range(0, 2*n, 2):
        bikeSpeed.append(max(bikeList[j], bikeList[j+1])) 
else:
    
    peg.reverse()

    for i in range(n):
        

        
        bikeList.append(dmoj[i])
        bikeList.append(peg[i])
        
    for j in range(0, 2*n, 2):
        bikeSpeed.append(max(bikeList[j], bikeList[j+1])) 


for a in bikeSpeed:
    total += int(a)

print(total)