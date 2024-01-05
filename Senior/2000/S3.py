#not finished
# IR ERROR

n = int(input())

nodeassign = {}
node = 0


graph = [[False for i in range(100)]for i in range(100)] 

for i in range(n):
    URL = input()
    HTMLcode = ''
    HTML = ''
    while HTML != "</HTML>":
        HTML = input()
        HTMLcode += HTML

    while HTMLcode.find("A HREF=") != -1:
        HTMLlink = HTMLcode.find("A HREF=")
        start = HTMLcode.find('"', HTMLlink)
        end = HTMLcode.find('"', start + 1)
        link = HTMLcode[start + 1: end]

        print("Link from", URL, "to", link)

        if URL not in nodeassign:
            nodeassign[link] = node
            node += 1
        if link not in nodeassign:
            nodeassign[link] = node
            node += 1
        
        graph[nodeassign[URL]][nodeassign[link]] = True
        HTMLcode = HTMLcode[end + 1:]

print()

here = input()
while here != "The End":
    there = input() 
    flag = [False for i in range(100)]
    queue = [nodeassign[here]]
    flag[nodeassign[here]] = True 
    end = nodeassign[there]
    while queue:
        u = queue.pop(0)
        for i in range(100): 
            if graph[u][i] and not flag[i]: 
                flag[i] = True
                queue.append(i)
    if flag[end]:
        print ("Can surf from", here, "to", there)
    else:
        print ("Can't surf from", here, "to", there) 
               
    here = input()