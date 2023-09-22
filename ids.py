#IDA algorithm similar to dfs but with limit increases
graph = {
    'a': ['b','c'],
    'b': ['d','e'],
    'c': ['f','g'],
    'd': [],
    'e': ['h','i'],
    'f': [],
    'g': [],
    'h': [],
    'i': []}
initial=input("Enter the initial state: ")
goal=input("Enter the goal state: ")
def ids(inital,goal):
    frontier=[]
    explored=[]
    count=0
    frontier.append(inital)
    while frontier:
        node=frontier.pop(0)
        explored.append(node)
        if node==goal:
            return explored,count
        adj=graph[node]
        for child in adj:
            if child not in frontier and child not in explored:
                frontier.append(child)
                frontier.reverse()
                count=count+1
ans=ids(initial,goal)

print("Goal state reached")

print("The path found by Iterative deepening search is : ",ans[0])
print("The depth is : ",ans[1])