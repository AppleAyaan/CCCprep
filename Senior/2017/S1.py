n = int(input())

x = input().split(' ')
y = input().split(' ')

a = []

x_total = 0
y_total = 0
l = False
for i in range(n):
    x_total += int(x[i])
    y_total += int(y[i])
    
    if x_total == y_total:
        a.append(i+1)
        l = True
        
    
if l != True:   
    print("0") 
else:
    print(max(a))