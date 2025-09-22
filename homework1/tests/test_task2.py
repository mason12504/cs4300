# Test data type operations
# Python usually just makes stuff work but things like + being concatenate on strings and so on is always different

import sys
import os

# this is weird but it is the only method I tried from geeksforgeeks and it works so it'll do  
# per https://www.geeksforgeeks.org/python/python-import-from-parent-directory/ 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current) 
parent = parent + "/src"
sys.path.append(parent)

from task2 import *

def test_int(): 
	# make sure it's an int
	assert(int(myInt) ==myInt)

def test_list():
	# verify you can add to a list of integers add them up and get an integer result
	sum = 0
	myList.append(myInt)
	for element in myList: # verify list iterating 
		sum = element + sum 
	# 1 + 19 + 4 + 9 + 20 = 53
	assert(sum == 53 )

def test_string(): 
	# very string iteration and concatenation
	assert(myString + " " + myString2 == "Hello World")
	# make sure you can iterate through both and basically compare two strings
	for l, m in zip(myString, "Hello"):
		assert(l == m)
	
	assert(myString == "Hello")

def test_float(): 
	# show imprecision
	assert(myFloat + 0.0000000000000001 == 9.345)
	# show operations 
	assert(myFloat + myFloat == 18.690)
	assert(myFloat/ 3 == 3.115)

def test_bool(): 
	# check boolean operations 
	assert((tBool and fBool) == False)
	assert((tBool and tBool) == True)
	assert((fBool and fBool) == False)

	assert(tBool or fBool == True)
	assert(tBool or tBool == True)
	assert(fBool or fBool == False)

	assert((not tBool) == False)
	assert((not fBool) == True)
