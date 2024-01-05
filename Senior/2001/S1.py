n = list(input())

a = n.index("C")
b = n.index("D")
c = n.index("H")
d = n.index("S")


total = 0
points = 0

print("Cards Dealt              Points")

print("Clubs", end = ' ')
for i in range(a+1, b):
    print(n[i], end = ' ')

    if n[i] == "A":
        points += 4
    elif n[i] == "K":
        points += 3
    elif n[i] == "Q":
        points += 2
    elif n[i] == "J":
        points += 1

if len(n[a+1:b]) == 0:
    points += 3
elif len(n[a+1:b]) == 1:
    points += 2
elif len(n[a+1:b]) == 2:
    points += 1

print("      ", points)
total += points
points = 0

print("Diamonds", end = ' ')
for j in range(b+1, c):
    print(n[j], end = ' ')
   
    if n[j] == "A":
        points += 4
    elif n[j] == "K":
        points += 3
    elif n[j] == "Q":
        points += 2
    elif n[j] == "J":
        points += 1

if len(n[b+1:c]) == 0:
    points += 3
elif len(n[b+1:c]) == 1:
    points += 2
elif len(n[b+1:c]) == 2:
    points += 1

print("      ", points)

total += points
points = 0

print("Hearts", end = ' ')
for k in range(c+1, d):
    print(n[k], end = ' ')
    
    if n[k] == "A":
        points += 4
    elif n[k] == "K":
        points += 3
    elif n[k] == "Q":
        points += 2
    elif n[k] == "J":
        points += 1

if len(n[c+1:d]) == 0:
    points += 3
elif len(n[c+1:d]) == 1:
    points += 2
elif len(n[c+1:d]) == 2:
    points += 1

print("      ", points)
total += points
points = 0

print("Spades", end = ' ')
for l in range(d+1, len(n)):
    print(n[l], end = ' ')
    
    if n[l] == "A":
        points += 4
    elif n[l] == "K":
        points += 3
    elif n[l] == "Q":
        points += 2
    elif n[l] == "J":
        points += 1

if len(n[d+1:len(n)]) == 0:
    points += 3
elif len(n[d+1:len(n)]) == 1:
    points += 2
elif len(n[d+1:len(n)]) == 2:
    points += 1

print("      ", points)

total += points

print("                   ", "Total", total)