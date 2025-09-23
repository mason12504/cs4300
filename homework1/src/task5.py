# task5
# Mason Andersen
# CS 4300

# This program prints books with list slicing

# List of my favorite books and authors
def bookListSlice():
    booksList = ["The Hobbit, J. R. R. Tolkien", 
                "The Lord of the Rings, J. R. R. Tolkien", 
                "Holes, Louis Sachar", 
                "Harry Potter and the Philosopher's Stone, J. K. Rowling"]
    print(booksList[0:3])
    return(booksList[0:3])
# dictionary as a basic student database

def createStudentDict():
    # just gonna join 2 lists for this
    studentList = ["Mason Andersen", "John Smith", "Amilia Earheart", "Jim Wiley", "Edgar Fitzjerald"]    
    IDList = [1, 2, 3, 4, 5]

    studentDict = dict(zip(studentList, IDList))
    return studentDict
    # names, ID



