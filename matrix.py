import numpy as np
def matrix_add(matrrixx,matrixx2):
    try:
        result  = np.add(matrrixx1,matrrixx2)
        return result
    except ValueError:
        return "Matrix dimension must be same"
def matrix_subtract(matrrixx1,matrixx2):
    try:
        result  = np.subtract(matrrixx1,matrrixx2)
        return result
    except ValueError:
        return "Matrix dimension must be same"
def matrix_mul(matrrixx1,matrixx2):
    try:
        result  = np.dot(matrrixx1,matrrixx2)
        return result
    except ValueError:
        return "Matrix dimension must be same"
