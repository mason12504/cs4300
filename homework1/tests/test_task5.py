# Test some control structures in python 

import sys
import os

# this is weird but it is the only method I tried from geeksforgeeks and it works so it'll do  
# per https://www.geeksforgeeks.org/python/python-import-from-parent-directory/ 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current) 
parent = parent + "/src"
sys.path.append(parent)

from task5 import * 

def test_slice():
    # first 3 entries of my list 
    assert(bookListSlice() == ["The Hobbit, J. R. R. Tolkien", "The Lord of the Rings, J. R. R. Tolkien", 
                "Holes, Louis Sachar"])

def test_dict(): 
    assert(createStudentDict()["Mason Andersen"] == 1)
    assert(createStudentDict()["Jim Wiley"] == 4)