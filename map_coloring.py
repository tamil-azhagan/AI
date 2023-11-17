#map coloring

def is_valid(map_assignemnt):
    p1,p2,p3,p4=map_assignemnt

    if p1==p2 or p1==p3 or p2==p3 or p2==p4 or p3==p4:
        return False
    return True

def backtracking(assignment):
    if (len(assignment))==4:
        if is_valid(assignment):
            return assignment
        return None
    
    for c in color :
        val=backtracking(assignment+[c])

        if val:
            return val
    return None

color=["Red","Green","Blue"]
ans=backtracking([])
if ans:
    c1,c2,c3,c4=ans
    print("Color of p1: ",c1)
    print("Color of p2: ",c2)
    print("Color of p3: ",c3)
    print("Color of p4: ",c4)

else:
    print("No solution")