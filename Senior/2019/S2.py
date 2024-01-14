#incomplete

x = int(input())

a = []

for i in range(x):
    final = []
    n = int(input())
    for num in range(2, n*n):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                a.append(num)
    
    l = 0
    r = len(a)-1
    for j in range(len(a)-1):
        if (a[l] + a[r]) / 2 < n:
            r -= 1
            if (a[l] + a[r]) / 2 < n:
                l += 1
        elif (a[l] + a[r]) / 2 == n:
            print(a[l], a[r])
    