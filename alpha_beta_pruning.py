#alpha beta #alpha_beta_pruning
import numpy as np
MIN=float("-inf")
MAX=float("inf")

def alpha_beta_pruning(depth,index,maximizingPlayer,values,alpha,beta):
    if (depth==0):
        return values[index]
    
    if maximizingPlayer:
        opti=MIN
        for i in range(0,2):
            val=alpha_beta_pruning(depth-1,index*2+i,False,values,alpha,beta)
            opti=max(opti,val)
            alpha=max(alpha,opti)

            if alpha>=beta:
                break
        return opti
    
    else:
        opti=MAX
        for i in range(0,2):
            val=alpha_beta_pruning(depth-1,index*2+i,True,values,alpha,beta)
            opti=min(opti,val)
            beta=min(beta,opti)

            if alpha>=beta:
                break
        return opti
    
values = [10,5,7,11,12,8,9,8,5,12,11,12,9,8,7,10]
depth=int(np.log2(len(values)))

ans=alpha_beta_pruning(depth,0,True,values,MIN,MAX)
print("The answer ppf alpha is: ",ans)