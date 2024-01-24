#INCOMPLETE
x = int(input())

first = input().split(' ')
last = input().split(' ')


paired = []

for i in range(x):
    if [first[i], last[i]] not in paired or first[i] not in paired or last[i] not in paired:
        paired.append([first[i], last[i]])

if len(paired) == x:
    print('good')
else:
    print('bad')