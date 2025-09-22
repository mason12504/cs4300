# Test some control structures in python 

import sys
import os

# this is weird but it is the only method I tried from geeksforgeeks and it works so it'll do  
# per https://www.geeksforgeeks.org/python/python-import-from-parent-directory/ 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current) 
parent = parent + "/src"
sys.path.append(parent)

from task4 import * 

# just one big test
def test_discount():
    
    # set up some values and edge cases like 0, 0.1, 1
    priceList = [0, 1, 100, 49.1, 50.9999, 10000]
    discountList = [100, 0.1, 0, -1, 50, 0.65] # negative discount behavior is basically a price increase
    expectedResultList = [0, 0.9, 100, 98.2, 25.49995, 3500]

    for price, discount, expectedResult in zip(priceList, discountList, expectedResultList):
        assert(calculate_discount(price, discount) == expectedResult)
