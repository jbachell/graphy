#John Bacheller
#MY CODE thank you very much

#TODO make the graph symetric maybe? also print format to match mathematica

import itertools

def is_valid(n, g):
    for x in range(n):
        for y in range(n - x - 1):
            if g[y + x + 1][x] == 1:
                if g[x][x] == g[y + x + 1][y + x + 1]:
                    return 0 #Coloring failed at least once
    return 1


colored = 0
checkingColoring = 1

numVert = input("Enter number of vertices: ")
temp = input("Would you like to check for coloring? (0 = Find Colorings, 1 = Check Colorings): ")
checkingColoring = int(temp)

#Varibles used
w, h = int(numVert), int(numVert)
graph = [[0 for x in range(w)] for y in range(h)]

# for x in range(w):
#     if checkingColoring == 1:
#         temp = input("Enter vertex " + str(x + 1) + " color:")
#         graph[x][x] = int(temp)
#     print("Enter what this vertex(" + str(x + 1) + ") is connected to, separated by spaces: ")
#     connectedEdges = list(map(int, input().split()))
#     connectedEdges.sort()
#     for y in connectedEdges:
#         if y - 1 > x:
#             graph[y - 1][x] = 1

graph = [[0,1,1,1,1],[1,0,1,1,1],[1,1,0,1,1],[1,1,0,0,1],[0,1,1,1,2]]


#OKAY THE GRAPH WAS TAKEN IN
if checkingColoring == 1:
    print("\nWe got the graph.  Checking for coloring.")
else:
    print("\nWe got the graph.  Generating a coloring")

if checkingColoring == 1:
    colored = is_valid(w, graph)
    if colored == 0:
        print("\nYou didn't color correctly!")
    else:
        print("\nGraph is correct")
#TRYING TO FIND A COLORING
if checkingColoring == 0:
    minColoring = 3 #w
    #setOfColors = range(minColoring)
    #colorPerm = itertools.product(range(minColoring), repeat=minColoring)
    #print(colorPerm)
    #for x in range(minColoring):
     #   setOfColors[x] = x
    count = 0
    for coloring in itertools.product(range(minColoring), repeat=minColoring):
        for y in range(minColoring):
            graph[y][y] = coloring[y]
        if is_valid(minColoring, graph) == 1:
            print("Found one")
            count = count+1
            #print(x)
            print(graph)
    print(count)






#for x in range(w):

#print(graph[0])
#print(graph)


# for y in range(w - x - 1):
#     if graph[y + x + 1][x] in connectedEdges:
#         graph[y + x + 1][x] = 1
#     else:
#         graph[y + x + 1][x] = 0
