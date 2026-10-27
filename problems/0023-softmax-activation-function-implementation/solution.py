import math

def softmax(scores: list[float]) -> list[float]:
    total=0
    Max=max(scores)
    for x in scores:
        total+=math.exp(x-Max)
    ans=[]
    for x in scores:
        ans.append(math.exp(x-Max)/total)
    return ans

    #Numerical stability
