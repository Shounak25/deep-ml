import numpy as np

def cross_product(a, b):
    # Your code here
    a1,a2,a3=a[0],a[1],a[2]
    b1,b2,b3=b[0],b[1],b[2]

    return [a2*b3-a3*b2,a3*b1-a1*b3,a1*b2-a2*b1]