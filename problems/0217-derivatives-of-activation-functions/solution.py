import math
def activation_derivatives(x: float) -> dict[str, float]:
    """
    Compute the derivatives of Sigmoid, Tanh, and ReLU at a given point x.
    
    Args:
        x: Input value
        
    Returns:
        Dictionary with keys 'sigmoid', 'tanh', 'relu' and their derivative values
    """
    # Your code here
    value=dict()
    value['sigmoid']=math.exp(-x)/((1+math.exp(-x))**2)
    value['tanh']=1-((math.exp(x)-math.exp(-x))/((math.exp(x))+math.exp(-x)))**2
    if x>0:
        value['relu']=1.0
    else:
        value['relu']=0.0
    return value
