import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """
    # Write code here
    if (type(x) == list):
        x  = np.asarray(x, dtype = float)
        x = np.multiply(x, np.asarray(np.array([-1 for i in range(len(x))]), dtype=float))
        x = np.exp(x)
        x = np.add(x, np.asarray(np.array([1 for i in range(len(x))]), dtype=float))
        x = np.divide(np.asarray(np.array([1 for i in range(len(x))]), dtype=float), x)
        return x
    else: 
        x *= -1
        x = np.exp(x)
        x = 1 + x
        x = 1/x
        return x
            
            
    pass