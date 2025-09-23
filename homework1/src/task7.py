# task7
# Mason Andersen
# CS 4300

# this file demonstrates importing a package and using its features
import numpy as np

# find the determinant of a matrix
def matrixDet(arr):
    arr = np.array(arr)
    # fix numpy floating point imprecision
    return round(np.linalg.det(arr), 4)

def matrixDotProduct(arr1, arr2):
    arr1 = np.array(arr1)
    arr2 = np.array(arr2)
    return np.dot(arr1, arr2)