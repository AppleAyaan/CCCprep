n = list(input())

grid = [[1, 2], [3, 4]]


for i in range(len(n)):
    if n[i] == "H":
        grid[0][0], grid[0][1] = grid[0][1], grid[0][0]
        grid[1][0], grid[1][1] = grid[1][1], grid[1][0]
    elif n[i] == "V":
        grid[0][0], grid[1][0] = grid[1][0], grid[0][0]
        grid[0][1], grid[1][1] = grid[1][1], grid[0][1]

for j in grid:
    for l in j:
        print(l, end = ' ')
    print('')
    
    