x = int(input())
a = int(input())
b = int(input())
c = int(input())

total = 0

while x > 0:
    x -= 1
    total += 1
    a += 1

    if a == 35:
        x += 30
        a = 0

    if x == 0:
        break

    x -= 1
    total += 1
    b += 1

    if b == 100:
        x += 60
        b = 0

    if x == 0:
        break
    
    x -= 1
    total += 1
    c += 1

    if c == 10:
        x += 9
        c = 0

print("Martha plays", total ,"times before going broke.")