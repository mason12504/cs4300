# Test some functions of the package numpy 

import sys
import os

# this is weird but it is the only method I tried from geeksforgeeks and it works so it'll do  
# per https://www.geeksforgeeks.org/python/python-import-from-parent-directory/ 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current) 
parent = parent + "/src"
sys.path.append(parent)

from task7 import * 

# test the determinant of a matrix
def testDet():
    # 2x2 matrices
    inputs = [
        [[1,2], [3,4]],
        [[19, 24], [30, 41]],
        [[0,0], [0,0]],
    ]
    results = [-2, 59, 0] # from online calculator https://www.emathhelp.net/calculators/linear-algebra/matrix-determinant-calculator/ 
    for arr, result in zip(inputs, results):
        assert(matrixDet(arr) == result)

# test the vector dot product
def testDot():
    # 4x1 vectors
    inputs1 = [
        [5,6, 7, 8],
        [1, 1, 1, 1],
        [[100, 90, 80, 70]],
    ]
    inputs2 = [
        [1,2, 3, 4],
        [19, 24, 30, 41],
        [0,0, 0,0],
    ]
    results = [70, 114, 0] # from online calculator https://www.emathhelp.net/calculators/linear-algebra/matrix-determinant-calculator/ 
    for arr1, arr2, result in zip(inputs1, inputs2, results):
        assert(matrixDotProduct(arr1, arr2) == result)