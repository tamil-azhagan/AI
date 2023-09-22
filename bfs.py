#BFS
graph={ 'E':['A','B','F'],
        'A':['B','C','D'],
        'B':['D'],
        'C':['D','L'],
        'D':['L'],
        'F':['L'],
        'L':['M'],
        'M':[]
      }
initial=input("Enter the initial node: ")
goal=input("Enter the goal node: ")

explored=[]
def bfs(initial,goal):
    frontier=[]
    frontier.append(initial)
    while frontier:
        node=frontier.pop(0)
        explored.append(node)
        if node==goal:
            return explored
        adj=graph[node]
        for child in adj:
            if child not in frontier and child not in explored:
                frontier.append(child)

ans=bfs(initial,goal)
print("The BFS visited path is :",ans)
