import numpy as np
def matrix_add(matrix1,matrix2):
    try:
        result  = np.add(matrix1,matrix2)
        return result
    except ValueError:
        return "Matrix dimension must be same"
def matrix_subtract(matrix1,matrix2):
    try:
        result  = np.subtract(matrix1,matrix2)
        return result
    except ValueError:
        return "Matrix dimension must be same"
def matrix_mul(matrix1,matrix2):
    try:
        result  = np.dot(matrix1,matrix2)
        return result
    except ValueError:
        return "Matrix are not suitable for multiplication "
if __name__ == "__main__":
    # matrix_a = np.random.randint(1, 10, size=(3, 3))
    # matrix_b = np.random.randint(1, 10, size=(3, 3))

    print("Matrix A:")
    print(matrix_a)

    print("Matrix B:")
    print(matrix_b)

    addition_result = matrix_add(matrix_a, matrix_b)
    print("Matrix Addition Result:")
    print(addition_result)

    subtraction_result = matrix_subtract(matrix_a, matrix_b)
    print("Matrix Subtraction Result:")
    print(subtraction_result)

    multiplication_result = matrix_mul(matrix_a, matrix_b)
    print("Matrix Multiplication Result:")
    print(multiplication_result)
