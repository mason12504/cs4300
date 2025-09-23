# Mason Andersen
# CS 4300

# Task 6: 
# this program reads an input file of text, and counts the number of words in it. 
import re


# used this resource https://www.geeksforgeeks.org/python/python-remove-punctuation-from-string/ for the regex
def readWordCount():

    wordCount = 0 

    with open('task6_read_me.txt', 'r') as file:
        # each line is read as a long string 
        for line in file:
            # remove the punctuation then .split() into individual words based on whitespace
            line = re.sub(r'[^\w\s]', '', line).split()
            # parse the words
            for word in line:
                wordCount = wordCount + 1
    
    return wordCount


