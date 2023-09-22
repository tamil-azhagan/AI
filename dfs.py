def dfs(inital,goal):
    frontier=[]
    explored=[]
    frontier.append(inital)
    while frontier:
        node=frontier.pop(0)
        explored.append(node)
        if node==goal:
            return explored
        adj=graph[node]
        for child in adj:
            if child not in frontier and child not in explored:
                frontier.append(child)
                frontier.reverse()

ans=dfs(initial,goal)
print("The DFS visited path is :",ans)
