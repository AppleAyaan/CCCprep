x = int(input())

flow = []

for i in range(x):
    flow.append(int(input()))

seventySeven = int(input())
while seventySeven != 77:
    #split
    if seventySeven == 99:
        a = int(input())
        flowNum = int(input())

        flow1 = (flow[a-1] * flowNum)/100
        flow2 = (flow[a-1] * (100-flowNum)) / 100 
        flow.pop(a-1)
        flow.insert(a-1, flow1)
        flow.insert(a, flow2)
    
    #join
    elif seventySeven == 88:
        b = int(input())
        flow1 = flow[b-1]
        flow2 = flow[b]
        flow3 = flow1 + flow2
        flow.pop(b-1)
        flow.pop(b-1)
        flow.insert(b-1, flow3)   

    
    seventySeven = int(input())

for num in flow:
    print(round(num), end = ' ')