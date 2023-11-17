graph={
    'S':['A','B','D'],
    'A':['B','G1'],
    'B':['A','C'],
    'C':['S','F','G2'],
    'D':['C','S','E'],
    'E':['G3'],
    'F':['D','G3'],
    'G1':[],
    'G2':[],
    'G3':[]
}
H={'S':5,'A':7,'B':3,'C':4,'D':6,'E':5,'F':6,'G1':0,'G2':0,'G3':0}
initial=input("Enter the initial state: ")
goal=input("Enter the goal state: ")

def gbfs(initial,H,goal):
    frontier=[]
    explored=[]
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
                frontier.sort(key=lambda child:H[child])
ans=gbfs(initial,H,goal)
print("The optimal path is: ",ans)