# Mason Andersen
# CS 4300
# Homework 1
# 9-22-2025

import sys
import os

# this is weird but it is the only method I tried from geeksforgeeks and it works so it'll do  
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current) 
parent = parent + "/src" 
sys.path.append(parent)

from task1 import *
def test_task1(): 
	assert printTask1() == "Hello World!" 
