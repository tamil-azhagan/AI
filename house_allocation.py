def is_valid(assignments):
    a,b,c,d=assignments

    if b==2 or c==1 or (a-d)!=1 or d>a or (a-c)!=2 :
        return False
    return True

def backtracking(assignments):
    if (len(assignments))==4:
        if is_valid(assignments):
            return assignments
        return None

    for i in range(1,5):
        result=backtracking(assignments + [i])

        if result:
            return result
    return None
    

family_assignment=backtracking([])
if family_assignment:
    a,b,c,d=family_assignment
    print(f"A lives in House {a}")
    print(f"B lives in House {b}")
    print(f"C lives in House {c}")
    print(f"D lives in House {d}")
else:
    print("No solution")


