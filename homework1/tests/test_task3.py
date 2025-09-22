# Test some control structures in python 

import sys
import os

# this is weird but it is the only method I tried from geeksforgeeks and it works so it'll do  
# per https://www.geeksforgeeks.org/python/python-import-from-parent-directory/ 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current) 
parent = parent + "/src"
sys.path.append(parent)

from task3 import * 

# test some values that are positive, negative, or zero
def test_if():
    for i in range(-25, -1):
        assert(pnz(i) == "-")
    for j in range(1, 25):
        assert(pnz(j) == "+")
    
    assert(pnz(0) == "0")

    # test if it's not given a number
    assert(pnz("hello" == None))

# make sure it actually got the first 10 primes 
def test_for():
    # these are the first 10 primes per google
    assert(printPrimes() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])

def test_while():
    # the sum of the first 100 numbers is 5050
    assert(sum100()==5050)