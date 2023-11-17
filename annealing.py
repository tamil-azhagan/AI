import random
import math
def fcost(sol):
    return sum([i**2 for i in sol])
def successor(sol,step=1.0):
    return [x+random.uniform(-step,step) for x in sol]
def sim_annealing(initsol, inittemp, alpha, iters):
    currsol, sol= initsol,initsol
    temp=inittemp
    cost=fcost(sol)
    mincost=cost

    for i in range(iters):
        neighbor=successor(currsol)
        ncost=fcost(neighbor)
        costdiff=ncost-cost

        if costdiff<0 or random.random() < math.exp(-costdiff/temp):
            currsol=neighbor
            cost=ncost

            if cost<mincost:
                sol=currsol
                mincost=cost
        temp*=alpha

    return sol,mincost
initsol=[300,400]
inittemp=1000
alpha=0.95
iters=500
best_sol,best_cost=sim_annealing(initsol,inittemp,alpha,iters)
print("The best solution is: ",best_sol)
print("The best cost is: ",best_cost)