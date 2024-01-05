n = int(input())

ans = 0
i = 0

while n >= i*5:
    if (n - i*5) % 4 == 0:
        ans +=1
    i += 1
print(ans)
