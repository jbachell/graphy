#John Bacheller
#MY CODE thank you very much

import random

w, h = 5, 5
graph = [[1 for x in range(w)] for y in range(h)]

listZ = []
listO = []
listT = []
remainder = []

print("Starting graph generation .")

for x in range(w):
    graph[x][x] = random.randint(0, 2)
    #print(".")
    if graph[x][x] == 0:
        listZ.append(x);
        for y in listZ:
            if x != y:
                graph[x][y] = 0
    elif graph[x][x] == 1:
        listO.append(x)
        for y in listO:
            if x != y:
                graph[x][y] = 0
    else:
        listT.append(x)
        for y in listT:
            if x != y:
                graph[x][y] = 0
    # print graph[x][x];

print("Graph Generated.")
message = input("What is your message?\n")

numMessage = ""
for x in message:
    numMessage = numMessage + str(ord(x))

x = 0
temp = int(numMessage)
while temp != 0:
    remainder.append(int(temp % 3))
    temp = int(temp/3)
    x += 1

print("{*} Message converted to number")
colorEncoding = random.randint(0, 2)
startingPoint = random.randint(0, w)
distance = random.randint(0, 1000)

#for x in range(w):
   # for y in range(h):
       # graph[x][y] = graph[x][y] * random.randint(0, 1000)

i = 0
x = 0
while i < distance:
    if x + startingPoint >= w - 1:
        x = 0
    if graph[startingPoint + x][startingPoint + x] == colorEncoding:
        i += 1
    x += 1

y = 0
graph[x][x] = 0
for y in remainder:
    graph[x][x] = y + graph[x][x]

for z in range(w):
    print("[", end="")
    for y in range(w):
        if y == (w-1):
            print(graph[z][y], end="")
        elif y != z:
            print(str(graph[z][y]) + ",", end="")
        else:
            print(str(0) + ",", end="")
    print("],", end="")
# for z in range(w):
#     for y in range(h):
#         if graph[z][y] == graph[x][x]:
#             for n in remainder:
#                 print(n, end="")
#         else:
#             print(graph[z][y], end="")

#print(graph)
#print graph[1][3];
#colorEncoding == graph[startingPoint][startingPoint]
#i += 1
#graph[startingPoint[0]][startingPoint[1]] = str(remainder[i])
#remainder.remove(remainder[i])
