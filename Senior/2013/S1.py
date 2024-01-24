x = input()




while True:
    unique = []

    x = int(x) + 1
    y = list(str(x))
    for i in range((len(y))):
        if y[i] not in unique:
            unique.append(y[i])

    if len(unique) == len(y):
        break
print(x)