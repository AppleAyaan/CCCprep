#not solved
#WA

n = input().split(' ')

print("Sun Mon Tue Wed Thr Fri Sat")

#first line
for i in range(int(n[0])- 1):
    print("   ", end = ' ')
for j in range(1, 9 - int(n[0])):
    print("%3i" % j, end = ' ')
print('\n', end = '')


for k in range(9 - int(n[0]), int(n[1]) - 17):
    print("%3i" % k, end = ' ')

print('\n', end = '')

for l in range(int(n[1]) - 17, int(n[1]) - 10): 
    print("%3i" % l, end = ' ')

print('\n', end = '')

for m in range(int(n[1]) - 10, int(n[1]) - 3): 
    print("%3i" % m, end = ' ')

print('\n', end = '')

for n in range(int(n[1]) - 3, int(n[1]) + 1 ):
    print("%3i" % n, end = ' ')

print('\n')
