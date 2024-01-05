x = input().split(' ')

n = int(x[0])
m = int(x[1])
k = int(x[2])

notes = []

for i in range(1, n+1):
    goodSamples = min(k - n + i, m)

    if goodSamples <= 0:
        break

    if goodSamples >= i:
        val = min(i, m)
        notes.append(val)
        k -= val

    else:
        notes.append(notes[-goodSamples])
        k -= goodSamples

if k != 0:
    print("-1")
else:
    for i in notes:
        print(i, end = ' ')