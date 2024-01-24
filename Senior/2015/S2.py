j = int(input())
a = int(input())

jerseys = []
request = []

satisfied_athletes = 0

for i in range(j):
    jerseys.append(input())



for k in range(a):
    x = input().split(' ')
    
    if x[0] == "S" and jerseys[int(x[1]) - 1] is not False:
        satisfied_athletes += 1
        jerseys[int(x[1]) - 1] = False
    elif x[0] == "M" and (jerseys[int(x[1]) - 1] == "M" or jerseys[int(x[1]) - 1] == "L"):
        satisfied_athletes += 1
        jerseys[int(x[1]) - 1] = False
    elif x[0] == "L" and jerseys[int(x[1]) - 1] == "L":
        satisfied_athletes += 1
        jerseys[int(x[1]) - 1] = False

print(jerseys)
print(satisfied_athletes)


#passes all test cases :0    
