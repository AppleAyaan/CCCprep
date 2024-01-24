x = list(input())
y = list(input())

for i in range(len(y)):
    if y[i] in x:
        a = x.index(y[i])
        x.pop(a)
    
for j in range(len(y)):
    if y[j] == "*":
        x.pop()

if len(x) == 0:
    print("A")
else:
    print("N")