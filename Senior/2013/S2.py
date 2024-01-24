#INCOMPLETE WRONG METHOD

weight = int(input())   # max weight bridge can hold
n = int(input()) # number of cars

ind_weight = []

for i in range(n):
    w = int(input())    #weight of the i'th railway car
    ind_weight.append(w)

total = 0
start_pos = 0

counter = 0
m = 1
while total <= weight:
    total = 0


    if start_pos == n - 4:
        break
        

    for j in range(start_pos, start_pos + 4):
        total += int(ind_weight[j])

    print(total)
    
    if m == 1:
        m = 0
        counter += 4
    else:
        counter += 1
    start_pos += 1
print(counter)