import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    if (type(x) == list):
        x  = np.asarray(x, dtype = float)
        x = np.multiply(x, -1)
        x = np.exp(x)
        x = np.add(x, 1)
        x = np.divide(1, x)
        return x
    else: 
        x *= -1
        x = np.exp(x)
        x = 1 + x
        x = 1/x
        return x
            
            
    pass