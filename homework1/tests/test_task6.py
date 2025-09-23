# Test reading a file and word counting 

import sys
import os 

# this is weird but it is the only method I tried from geeksforgeeks and it works so it'll do  
# per https://www.geeksforgeeks.org/python/python-import-from-parent-directory/ 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current) 
parent = parent
sys.path.append(parent)

from task6 import * 

def testWordCount():
    # 104 from google docs word counting
    assert(readWordCount() == 104)
